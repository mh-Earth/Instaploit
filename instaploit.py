import os,sys,time
from itertools import islice
from math import ceil
from terminaltables import DoubleTable
import instaloader
from instapy import InstaPy
from comparison import comparisonID
from instapy import smart_run
from banner import randomBanners,ranbomTips
from getpass import getpass



exit_msg = "\033[91m\n[++] Shutting down ... Goodbye. (^_^)／\n\033[91m"
def banner():
    print(f"\033[91m[++]Tips:{ranbomTips()}\033[91m")                        
    print(randomBanners())
    print('''
                      _________ _\|/_ Powered by instaloader _\|/_ ______________
    ''')
def main():
    banner()
    global insta
    insta = instaloader.Instaloader()
    startUp = input("\033[92mLogin or continue as a guest(l or g)::\033[92m")
    if startUp == "l":
        global username,password
        username = input("\033[92m[+]Enter instagram username::\033[92m")
        try:
            insta.load_session_from_file(username)
        except FileNotFoundError:
            password = getpass("\033[92m[+]Enter instagram password::\033[92m")
            try:
                insta.login(username,password)
                insta.save_session_to_file()
                print("\033[92m[+]Loggin Successful!\033[92m")
            except Exception as e:
                print(f"\033[91m{e}\033[91m")
                print("\033[91m[!]Login failed....\033[91m")
                main()
                
        try:
            print("""\033[93m
┌════════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                        █
█                You can download or do any thing with this login account                █
█                                                                                        █
└════════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
            global session
            print("\033[92m[+]Successful restore session\033[92m")
            modulesForLogin()
            Login()
        except Exception as e:
            print(e)
            main()
    elif startUp == "g":
        print("\033[92m[+]Loading files....\033[92m")
        print("\033[92m[+]Loading modules....\033[92m")
        time.sleep(1)
        print("""\033[93m
┌════════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                        █
█                          The targeted account must be public                           █
█                                                                                        █
└════════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
        global target
        target = input("\033[92m[+]Enter target user name::\033[92m")
        Guest()
    elif startUp == "exit":
        sys.exit(exit_msg)
    else:
        print("\033[91m[!]Invalid option\033[91m")
        main()
    main()
# _________________________________________________________________________
def Login():
     
    try:
        module = input("\n\033[91m[{M}]\033[92m Chose a module::\033[92m")
        module = module.lower()
        if module == "":
            print("\n\033[91m[{M}]\033[92m Chose a module::\033[92m")
        elif module == "exit":
            sys.exit(exit_msg)
        elif module == "home":
            main()
        elif module == "help":
            modulesForLogin()
    # ___________________________________________________________________________
    # ___________________________________________________________________________
    # ___________________________________________________________________________
    # ___________________________________________________________________________
    # ___________________________________________________________________________

        elif module == "downp":
            modulesForDownp()
            def downp():
                global username,insta
                module = input("\n\033[91m[{M}]\033[92m Chose a module::\033[92m")

                if module == "df":
                    print("""\033[93m
┌══════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                      █
█                     Download everything from a profile with caption                  █
█                                                                                      █
█                  The account must be public or you follow that account               █
█                                                                                      █
└══════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                    targetId = input("\033[92m[+]Enter the user name to download::\033[92m")
                    if targetId == "back":
                        downp()
                    elif targetId == "exit":
                        sys.exit(exit_msg)
                    elif targetId == "home":
                        main()
                    elif targetId == "help":
                        modulesForDownp()
                    else:    
                        os.system(f"instaloader profile -l {username} --no-metadata-json --no-compress-json --igtv --saved --highlights --tagged {targetId}")
                        input("\033[92m[+]Press enter to continue \033[92m")
                    
                elif module == "dpp":
                    print("""\033[93m
┌══════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                      █
█                                Download the profile pic                              █
█                                                                                      █
└══════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                    def dpp():
                        targetId = input("\033[92m[+]Enter the user name to download::\033[92m")
                        if targetId == "back":
                            downp()
                        elif targetId == "exit":
                            sys.exit(exit_msg)
                        elif targetId == "home":
                            main()
                        elif targetId == "help":
                            modulesForDownp()
                            dpp()
                        else:    
                            os.system(f"instaloader -l {username} --no-posts --no-video-thumbnails --no-metadata-json --no-compress-json --no-captions --no-videos  {targetId}")
                            input("\033[92m[+]Press enter to continue \033[92m")
                    dpp()

                elif module == "dmrp":
                    print("""\033[93m
┌══════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                      █
█                              Download the most recent post                           █
█                                                                                      █
█                 The account must be public or you follow that account                █
█                                                                                      █
└══════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                    targetId = input("\033[92m[+]Enter the user name to download::\033[92m")
                    if targetId == "back":
                        downp()
                    elif targetId == "exit":
                        sys.exit(exit_msg)
                    elif targetId == "home":
                        main()
                    elif targetId == "help":
                        modulesForDownp()
                    else:    
                        posts = instaloader.Profile.from_username(insta.context, targetId).get_posts()
                        for post in posts:
                            insta.download_post(post, targetId)
                            break
                        input("\033[92m[+]Press enter to continue \033[92m")
                    
                elif module == "dap":
                    print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                                   Download all post                                 █
█                                                                                     █
█                  The account must be public or you follow that account              █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                    targetId = input("\033[92m[+]Enter the user name to download::\033[92m")
                    if targetId == "back":
                        downp()
                    elif targetId == "exit":
                        sys.exit(exit_msg)
                    elif targetId == "home":
                        main()
                    elif targetId == "help":
                        modulesForDownp()
                    else:    
                        os.system(f"instaloader -l {username} --no-videos --no-video-thumbnails --no-metadata-json --no-compress-json --no-captions  {targetId}")
                        input("\033[92m[+]Press enter to continue \033[92m")
                    
                elif module == "app":
                    print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                       Download a particular post with shortcode                     █
█                                                                                     █
█                  The account must be public or you follow that account              █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                    def app():
                        print("\033[92m[+]Enter '--help' for help\033[92m")
                        ShortCode = input("\033[92m[+]Enter post shortcode ::\033[92m")
                        if ShortCode == "back":
                            downp()
                        elif ShortCode == "exit":
                            sys.exit(exit_msg)
                        elif ShortCode == "home":
                            main()
                        elif ShortCode == "help":
                            downp()
                        elif ShortCode == "--help":
                            print("\033[92m[+]Visit https://elfsight.com/blog/2015/10/how-to-get-instagram-photo-shortcode get post short code\033[92m")
                            app()
                        elif ShortCode == "help":
                            modulesForDownp()
                        else:    
                            os.system(f"instaloader -- -{ShortCode}")
                            input("\033[92m[+]Press enter to continue \033[92m")
                        app()

                    app()

                elif module == "tap":
                    print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                                  Download tagged post                               █
█                                                                                     █
█                   The account must be public or you follow that account             █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                    targetId = input("\033[92m[+]Enter the user name to download::\033[92m")
                    if targetId == "back":
                        downp()
                    elif targetId == "exit":
                        sys.exit(exit_msg)
                    elif targetId == "home":
                        main()
                    elif targetId == "help":
                        modulesForDownp()
                    else:    
                        os.system(f"instaloader --l {username}  --no-profile-pic --no-posts --no-metadata-json --no-compress-json --no-captions --no-videos --tagged {targetId}")
                        input("\033[92m[+]Press enter to continue \033[92m")

                elif module == "hap":
                    print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                                  Download highlights                                █ 
█                                                                                     █
█                The account must be public or you follow that account                █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                    targetId = input("\033[92m[+]Enter the user name to download::\033[92m")
                    if targetId == "back":
                        downp()
                    elif targetId == "exit":
                        sys.exit(exit_msg)
                    elif targetId == "home":
                        main()
                    elif targetId == "help":
                        modulesForDownp()
                    else:    
                        os.system(f"instaloader -l {username} --no-posts --no-video-thumbnails --no-metadata-json --no-compress-json --no-captions --no-videos --highlights {targetId}")
                        input("\033[92m[+]Press enter to continue \033[92m")

                elif module == "gap":
                    print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                              Download all igtv videos                               █
█                                                                                     █
█                 The account must be public or you follow that account               █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                    targetId = input("\033[92m[+]Enter the user name to download::\033[92m")
                    if targetId == "back":
                        downp()
                    elif targetId == "exit":
                        sys.exit(exit_msg)
                    elif targetId == "home":
                        main()
                    elif targetId == "help":
                        modulesForDownp()
                    else:    
                        os.system(f"instaloader -l {username} --no-posts --no-metadata-json --no-compress-json --no-captions --igtv {targetId}")
                        input("\033[92m[+]Press enter to continue \033[92m")

                elif module == "vap":
                    print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                                     Download video                                  █
█                                                                                     █
█                           Downloa all video from a profile                          █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                    targetId = input("\033[92m[+]Enter the user name to download::\033[92m")
                    if targetId == "back":
                        downp()
                    elif targetId == "exit":
                        sys.exit(exit_msg)
                    elif targetId == "home":
                        main()
                    elif targetId == "help":
                        modulesForDownp()
                    else:    
                        os.system(f"instaloader -l {username} --no-pictures --no-video-thumbnails --no-metadata-json --no-compress-json --no-captions  --igtv {targetId}")
                        input("\033[92m[+]Press enter to continue \033[92m")

                elif module == "uap":
                    print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                          Update your local copy of a profiles                       █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                    targetId = input("\033[92m[+]Enter the user name to download::\033[92m")
                    if targetId == "back":
                        downp()
                    elif targetId == "exit":
                        sys.exit(exit_msg)
                    elif targetId == "home":
                        main()
                    elif targetId == "help":
                        modulesForDownp()
                    else:    
                        os.system(f"instaloader -l {username} --fast-update profile {targetId}")
                        input("\033[92m[+]Press enter to continue \033[92m")

                elif module == "fap":
                    print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                            Download the login profile's feed                        █
█                                                                                     █
█                            Dowload every thing from the feed                        █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                    os.system(f"instaloader -l {username} :feed --no-metadata-json --no-compress-json --no-captions")
                    input("\033[92m[+]Press enter to continue \033[92m")

                elif module == "sap":
                    print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                       Download the login profile's saved post                       █
█                                                                                     █
█                         Dowload every thing from the feed                           █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                    os.system(f"instaloader -l {username} :saved --no-metadata-json --no-compress-json --no-captions")
                    input("\033[92m[+]Press enter to continue \033[92m")

                elif module == "dmpp":
                    def dmpp():
                        print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                       Download the must popular post of a account                   █
█                                                                                     █
█                  The account must be public or you follow that account              █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                        targetId = input("\033[92m[+]Enter the user name to download post::\033[92m")
                        X_percentage = 1

                        profile = instaloader.Profile.from_username(insta.context, targetId)
                        posts_sorted_by_likes = sorted(profile.get_posts(),
                                                    key = lambda p: p.likes + p.comments,
                                                    reverse = True)

                        for post in islice(posts_sorted_by_likes, ceil(profile.mediacount * X_percentage / 100)):
                            print(f"\033[93m[+]Post link::{post.url}\033[93m")
                            insta.download_post(post, targetId)
                            break
                        dmpp()
                    dmpp()
                elif module == "help":
                    modulesForDownp()

                elif module == "exit":
                    sys.exit(exit_msg)
                
                elif module == "back":
                    Login()
                
                elif module == "home":
                    main()
                else:
                    print(f"\033[91m[!]'{module}' module not found\033[91m")

                downp()

            downp()
    # ___________________________________________________________________________
    # ___________________________________________________________________________
    # ___________________________________________________________________________
    # ___________________________________________________________________________
    # ___________________________________________________________________________
    # ___________________________________________________________________________
        elif module == "nfbi":
            def nfbi():
                print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                          List out all non-follow back ids                           █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                def unfollowNFBI():   
                    DoUnfollow = input(f"\033[92mDo you want to unfollow these user(y or n)::\033[92m")

                    if DoUnfollow == "y":
                        unfllw = input("\033[93mDo want to unfollow these users(y or n)::\033[93m")
                        if unfllw == "y":
                            try:
                                session = InstaPy(username = username,
                                                password = password,
                                                headless_browser = True)
                            except Exception as e:
                                password = getpass("\033[92m[+]Enter instagram passowrd\033[92m")
                                session = InstaPy(username = username,
                                                password = password,
                                                headless_browser = True)

                            with smart_run(session):
                                print("\033[93mUnfollowing all non-follow back uses please wait::\033[93m")
                                lis = coutomList
                                session.unfollow_users(amount = len(lis),custom_list_enabled = True,custom_list = lis,custom_list_param = "nonfollowers",)

                        elif DoUnfollow=="n":
                            pass

                        else:
                            print("\033[91m[!]Invalid options\033[91m")
                            unfollowNFBI()
                    elif DoUnfollow=="n":
                        pass

                    else:
                        print("\033[91m[!]Invalid options\033[91m")
                        unfollowNFBI()
                 
                insta.check_profile_id(username)
                global profile
                profile = instaloader.Profile.from_username(insta.context, username = username)
                followers = set(profile.get_followers())
                following = set(profile.get_followees())
                unfollowers = following - followers
                count = 0
                coutomList = []
                for users in unfollowers:
                    coutomList.append(users.username)
                    print(users.username)

                print(f"\033[92m[+]Total non follow-back followings {len(unfollowers)}\033[92m") 
                unfollowNFBI()
                input("\033[92m[+]Press enter to continue \033[92m")
                Login()
            nfbi()
    # ___________________________________________________________________________

        elif module == "gfls":
            def gfls():
                print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                             List out all Followers & following                      █
█                                                                                     █
█                   The account must be public or you follow that account             █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                targetId=input("\033[92m[+]Enter target name::\033[92m")
                run = input("\033[92m[+]Enter run for use the module::\033[92m")
                if run == "back":
                    downp()
                elif run == "exit":
                    sys.exit(exit_msg)
                elif run == "home":
                    main()
                elif run == "help":
                    modulesForLogin()
                elif run=="run":
                    print("\033[92m[+]Getting follower & following list..........\033[92m")
                    insta.check_profile_id(username)
                    profile = instaloader.Profile.from_username(insta.context, username = username)
                    followers = profile.get_followers()
                    following = profile.get_followees()

                    print(f"\033[93m[+]Total followers {profile.get_followers().count}:\033[93m")
                    print(f"\033[93m[+]Total followers {profile.get_followees().count}:\033[93m")
                    if profile.get_followers().count>500 or profile.get_followees().count>500:
                        limit = int(input("\033[93m[+]Enter a limit for safety::\033[93m"))
                        
                    elif following.count<followers.count:
                        limit = followers.count
                        print(limit)
                    else:
                        limit = following.count
                        print(limit)
                    
                    # ____________________________________________
                    
                    print("\033[93m[+]List of followers:\033[93m")
                    for index,users in enumerate(followers):
                        print(f'\033[97m{index+1}.{users.username}\033[97m')
                        index+= 1
                        if index>limit:
                            break
                    # ____________________________________________

                    print("\033[93m[+]List of following:\033[93m")
                    for index,users in enumerate(following):
                        print(f'\033[97m{index+1}.{users.username}\033[97m')
                        index+= 1
                        if index>limit:
                            break
                    # ____________________________________________

                    input("\033[92m[+]Press enter to continue \033[92m")
                    Login()
                else:
                    print("\033[91m[!]Invalid option\033[91m")
                    gfls()

            gfls()

        elif module == "scf":
            print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                Search a user from someone else following or follower                █
█                                                                                     █
█                The account must be public or you follow that account                █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
            targetID = input("\033[92m[+]Enter target ID (The account must be public or you follow that account)\n::\033[92m")
            run = input("\033[92m[+]Enter run for use the module::\033[92m")
            if run == "back":
                Login()
            elif run == "exit":
                sys.exit(exit_msg)
            elif run == "home":
                main()
            elif run == "help":
                modulesForLogin()
            elif run=="run":
                def scf():
                    searchFor = input("\033[92m[+]Search in follower or following::")
                    if searchFor == "following":
                        insta.check_profile_id(targetID)

                        print(f"\033[92m[+]Getting following list of {targetID}\033[92m")

                        searchID = input(f"\033[92m[+]Enter ID to search in {targetID} following::\033[92m")     

                        profile = instaloader.Profile.from_username(insta.context, username = targetID)

                        followingC = profile.get_followees().count

                        print(f"\033[93m[+]Searching {searchID} in {targetID}'s following\033[93m")

                        print(f"\033[93m[+]This process will take {(followingC/50)/60} minutes or more\n\033[93m")
                        NotFound=True
                        for index,user in enumerate(profile.get_followees()):
                            if user.username == searchID:
                                print(f"[+]{index+1}.{targetID} follow {user.username}")
                                NotFound=False
                                break
                        if NotFound:
                            print(f"[+]{targetID} don't follow {user.username}")



                    elif searchFor == "follower":
                        insta.check_profile_id(targetID)

                        print(f"\033[92m[+]Getting followers list of {targetID}\033[92m")

                        searchID = input(f"\033[92m[+]Enter ID to search in {targetID} following::\033[92m")     

                        profile = instaloader.Profile.from_username(insta.context, username = targetID)

                        print(f"\033[92m[+]Getting followers {targetID}\033[92m")
                        
                        followerC = profile.get_followers().count

                        print(f"\033[93m[+]Searching {searchID} in {targetID}'s followers\n\033[93m")

                        print(f"\033[93m[+]This process will take {(followerC/50)/60} minutes or more\n\033[93m")

                        NotFound=True
                        for index,user in enumerate(profile.get_followers()):
                            if user.username == searchID:
                                print(f"[+]{index+1.}{targetID} followed by {user.username}")
                                NotFound=False
                                break
                        if NotFound:
                            print(f"[+]{targetID} don't followed by{user.username}")

                    elif searchFor == "back":
                        Login()
                    elif searchFor == "home":
                        main()
                    elif searchFor == "exit":
                        sys.exit(exit_msg)
                    else:
                        print(f"\033[93m[!]Invalid option\n\033[93m")
                        scf()

                    print(f"\033[93m[+]Searching complete\n\033[93m")
                    input("\033[92m[+]Press enter to continue\n\033[92m")
                    
            scf()
        elif module == "rmlog":
            def rmlog():
                print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                                Remove all login logs                                █ 
█                                                                                     █
█            After removeing all log the programm will closed automatically           █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                run = input("\033[92m[+]Enter run for use the module::\033[92m")
                if run == "back":
                    main()
                elif run == "exit":
                    sys.exit(exit_msg)
                elif run == "home":
                    main()
                elif run == "help":
                    modulesForLogin()
                elif run == "run":
                    print("\033[92m[+]Removeing all login information\033[92m")
                    os.system(f"rm -r ~/.config/instaloader/session-{username}")
                    print("\033[92m[+]Done\033[92m")
                    input("\033[92m[+]Press enter to continue \033[92m")
                    sys.exit(exit_msg)
                else:
                    print("\033[91m[!]Invalid option\n\033[91m")
                    rmlog()

            rmlog()
    
        elif module == "ghostf":
            def ghostf():
                print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                             List out all Ghost Followers                            █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘\033[93m """)

                profile = instaloader.Profile.from_username(insta.context, username)

                likes = set()
                t1 = time.time()
                print(f"\033[93m[+]Fetching likes of all posts of profile {username}\033[93m.")
                print(f"\033[93m[+]This process may take some time according to {username} amount of post\033[93m.")
                for post in profile.get_posts():
                    print(f"\033[92m[+]{post}\033[92m")
                    likes = likes | set(post.get_likes())

                print(f"\033[93m[+]Fetching followers of profile {username}.\033[93m")
                followers = set(profile.get_followers())

                ghosts = followers - likes

                print("\033[93m[+]Storing ghosts into file.....\033[93m")
                with open("inactive-users.txt", 'w') as f:
                    for ghost in ghosts:
                        print(ghost.username, file = f)
                print("\033[92m[+]Done\033[92m")
                print("\033[92m[+]All ghost follower id stored in inactive-users.txt\033[92m")
                t2 = time.time()
                print(f"\033[92m[+]Finished in {t1-t2}s\033[92m")
                input("\033[92m[+]Press enter to continue \033[92m")
                Login()
            ghostf()
        elif module == "fllw":
            def fllw():
                global password
                print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                                   Follow a account                                  █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                try:
                    print("\033[92m[+]Enter the user name you want to unfollow(for follow multiple profile enter user  names like this:user1|user2|user3|user4.....)\033[92m")
                    ToFollow = input("\033[92m::\033[92m")
                    if ToFollow == "back":
                        Login()
                    elif ToFollow == "exit":
                        sys.exit(exit_msg)
                    else:
                        try:
                            ToFollow = ToFollow.split("|")
                        except Exception as TypeError:
                            pass
                        try:
                            session = InstaPy(username = username,
                                            password = password,
                                            headless_browser = True)
                        except Exception as e:
                            password = getpass("\033[92m[+]Enter instagram password:")
                            session = InstaPy(username = username,
                                            password = password,
                                            headless_browser = True)
                        except Exception as f:
                            print(f)

                        with smart_run(session):
                            lis = ToFollow
                            session.follow_by_list(followlist = lis,times = 1,sleep_delay = 30)
                        
                    input("\033[92m[+]Press enter to continue \033[92m")
                except Exception as e:
                    print(e)
                    print("\033[92m[!]Invalid input type\n\033[92m")
                    Login()
                fllw()
            fllw()
        elif module == "ufllw":
            def ufllw():
                global password
                print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                                   Unfollow a account                                █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                try:
                    print("\033[92m[+]Enter the user name you want to unfollow(for follow multiple profile enter user  names like this:user1|user2|user3|user4.....)\033[92m")
                    ToUnfollow = input("\033[92m::\033[92m")
                    if ToUnfollow == "back":
                        Login()
                    elif ToUnfollow == "exit":
                        sys.exit(exit_msg)
                    else:
                        try:
                            ToUnfollow = ToUnfollow.split("|")
                        except Exception as TypeError:
                            pass
                        try:
                            session = InstaPy(username = username,
                                            password = password,
                                            headless_browser = True)
                        except Exception as passwordNotFound:
                            password = getpass("\033[92m[+]Enter instagram password:")
                            session = InstaPy(username = username,
                                            password = password,
                                            headless_browser = True)

                        with smart_run(session):
                            lis = ToUnfollow
                            session.unfollow_users(amount = len(lis),custom_list_enabled = True,custom_list = lis,custom_list_param = "all",)
                    input("\033[92m[+]Press enter to continue \033[92m")
                except Exception as e:
                    print(f"\033[91m[!]{e}\033[91m")
                    print("\033[91m[!]Invalid input type\n\033[91m")
                    Login()
                ufllw()
            ufllw()
        elif module == "adcm":
            def adcm():
                print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                       An advance comparison beteewn two id                          █
█                                                                                     █
█                The account must be public or you follow that account                █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                
                profile1 = input("\033[93m[+]Enter first ID::\033[93m")
                profile2 = input("\033[93m[+]Enter second ID::\033[93m")
                
                comparisonID(profile1,profile2,username)
                input("\033[92m[+]Press enter to continue \033[92m")
            adcm()
        elif module == "exit":
            sys.exit(exit_msg)

        elif module == "back":
            main()

        elif module == "help":
            modulesForLogin()
        else:
            print(f"\033[91m[!]'{module}' module not found\033[91m")
            Login()

        Login()
    except Exception as e:
        print(f"[!]{e}")
        Login()
# _____________________________________________________________________________________________________
# _____________________________________________________________________________________________________
# _____________________________________________________________________________________________________
# _____________________________________________________________________________________________________
# _____________________________________________________________________________________________________
# _____________________________________________________________________________________________________
# _____________________________________________________________________________________________________

def Guest():
    global insta,target
    modulesForGuest()
    module = input("\n\033[91m[{M}]\033[92m Chose a module::\033[92m")
    module=module.lower()
    if module == "":
        print("\n\033[91m[{M}]\033[92m Chose a module::\033[92m")
    elif module == "exit":
        sys.exit(exit_msg)
    elif module == "home":
        main()
    elif module == "help":
        modulesForLogin()
# ___________________________________________________________________________
    elif module == "downt":
        def downt():
            global insta,target
            modulesForDownt()
            module = input("\n\033[91m[{M}]\033[92m Chose a module::\033[92m")

            if module == "df":
                print("""\033[93m
┌══════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                      █
█                         Download all post and video with caption                     █
█                                                                                      █
█                               The account must be public                             █
█                                                                                      █
└══════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                print(f"\033[93mTarget = {target}\033[93m")
                run = input(f"\033[92m[+]Enter run for use the module(target = {target})::\033[92m")
                if run == "back":
                    downt()
                elif run == "exit":
                    sys.exit(exit_msg)
                elif run == "home":
                    main()
                elif run == "help":
                    modulesForDownt()
                else:    
                    os.system(f"nstaloader profile --no-metadata-json --no-compress-json --igtv --saved --highlights --tagged {target}")
                    input("\033[92m[+]Press enter to continue \033[92m")
                
            elif module == "dpp":
                print("""\033[93m
┌══════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                      █
█                                Download the profile pic                              █
█                                                                                      █
└══════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                print(f"\033[93mTarget = {target}\033[93m")
                run = input("\033[92m[+]Enter run for use the module::\033[92m")
                if run == "back":
                    downt()
                elif run == "exit":
                    sys.exit(exit_msg)
                elif run == "home":
                    main()
                elif run == "help":
                    modulesForDownt()
                else:    
                    os.system(f"instaloader --no-posts --no-video-thumbnails --no-metadata-json --no-compress-json --no-captions --no-videos  {target}")
                    input("\033[92m[+]Press enter to continue \033[92m")

            elif module == "dmrp":
                print("""\033[93m
┌══════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                      █
█                              Download the most recent post                           █
█                                                                                      █
█                               The account must be public                             █
█                                                                                      █
└══════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                print(f"\033[93mTarget = {target}\033[93m")
                run = input("\033[92m[+]Enter run for use the module::\033[92m")
                if run == "back":
                    downt()
                elif run == "exit":
                    sys.exit(exit_msg)
                elif run == "home":
                    main()
                elif run == "help":
                    modulesForDownt()
                else:    
                    posts = instaloader.Profile.from_username(insta.context, target).get_posts()
                    for post in posts:
                        insta.download_post(post, target)
                        break
                    input("\033[92m[+]Press enter to continue \033[92m")
                
            elif module == "dap":
                print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                                  Download all post                                  █
█                                                                                     █
█                              The account must be public                             █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                print(f"\033[93mTarget = {target}\033[93m")
                run = input("\033[92m[+]Enter run for use the module::\033[92m")
                if run == "back":
                    downt()
                elif run == "exit":
                    sys.exit(exit_msg)
                elif run == "home":
                    main()
                elif run == "help":
                    modulesForDownt()
                else:    
                    os.system(f"instaloader --no-videos --no-video-thumbnails --no-metadata-json --no-compress-json --no-captions  {target}")
                    input("\033[92m[+]Press enter to continue \033[92m")
                
            elif module == "app":
                print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                       Download a particular post with shortcode                     █
█                                                                                     █
█                              The account must be public                             █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                def app():
                    print(f"\033[93mTarget = {target}\033[93m")
                    print("\033[92m[+]Enter '--help' for help\033[92m")
                    ShortCode = input("\033[92m[+]Enter post shortcode ::\033[92m")
                    if ShortCode == "back":
                        downt()
                    elif ShortCode == "exit":
                        sys.exit(exit_msg)
                    elif ShortCode == "home":
                        main()
                    elif ShortCode == "help":
                        downt()
                    elif ShortCode == "--help":
                        print("\033[92m[+]Visit https://elfsight.com/blog/2015/10/how-to-get-instagram-photo-shortcode get post short code\033[92m")
                        app()
                    elif ShortCode == "help":
                        modulesForDownt()
                    else:    
                        os.system(f"instaloader -- -{ShortCode}")
                        input("\033[92m[+]Press enter to continue \033[92m")
                    app()

                app()

            elif module == "tap":
                print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                                  Download tagged post                               █
█                                                                                     █
█                               The account must be public                            █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                print(f"\033[93mTarget = {target}\033[93m")
                run = input("\033[92m[+]Enter run for use the module::\033[92m")
                if run == "back":
                    downt()
                elif run == "exit":
                    sys.exit(exit_msg)
                elif run == "home":
                    main()
                elif run == "help":
                    modulesForDownt()
                else:    
                    os.system(f"instaloader --no-profile-pic --no-posts --no-metadata-json --no-compress-json --no-captions --no-videos --tagged {target}")
                    input("\033[92m[+]Press enter to continue \033[92m")

            elif module == "gap":
                print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                              Download all igtv videos                               █
█                                                                                     █
█                             The account must be public                              █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                print(f"\033[93mTarget = {target}\033[93m")
                run = input("\033[92m[+]Enter run for use the module::\033[92m")
                if run == "back":
                    downt()
                elif run == "exit":
                    sys.exit(exit_msg)
                elif run == "home":
                    main()
                elif run == "help":
                    modulesForDownt()
                else:    
                    os.system(f"instaloader --no-posts --no-metadata-json --no-compress-json --no-captions --igtv {target}")
                    input("\033[92m[+]Press enter to continue \033[92m")

            elif module == "vap":
                print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                           Downloa all video from a profile                          █
█                                                                                     █
█                              The account must be public                             █
█                                                                                     █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                print(f"\033[93mTarget = {target}\033[93m")
                run = input("\033[92m[+]Enter run for use the module::\033[92m")
                if run == "back":
                    downt()
                elif run == "exit":
                    sys.exit(exit_msg)
                elif run == "home":
                    main()
                elif run == "help":
                    modulesForDownt()
                else:    
                    os.system(f"instaloader --no-pictures --no-video-thumbnails --no-metadata-json --no-compress-json --no-captions  --igtv {target}")
                    input("\033[92m[+]Press enter to continue \033[92m")


            elif module == "dmpp":
                def dmpp():
                    print("""\033[93m
┌═════════════════════════════════════════════════════════════════════════════════════┐
█                                                                                     █
█                       Download the must popular post of a account                   █
█                                                                                     █
█                              The account must be public                             █
└═════════════════════════════════════════════════════════════════════════════════════┘ \033[93m""")
                    print(f"\033[93mTarget = {target}\033[93m")
                    run = input("\033[92m[+]Enter run for use the module post::\033[92m")
                    if run == "back":
                        downt()
                    elif run == "exit":
                        sys.exit(exit_msg)
                    elif run == "home":
                        main()
                    elif run == "help":
                        modulesForDownt()
                    elif run == "run":
                        X_percentage = 1

                        profile = instaloader.Profile.from_username(insta.context, target)
                        posts_sorted_by_likes = sorted(profile.get_posts(),
                                                    key = lambda p: p.likes + p.comments,
                                                    reverse = True)

                        for post in islice(posts_sorted_by_likes, ceil(profile.mediacount * X_percentage / 100)):
                            print(f"\033[93m[+]Post link::{post.url}\033[93m")
                            insta.download_post(post, target)
                            print("\033[92m[+]Download complete\033[92m")
                            time.sleep(1)
                            break
                    else:
                        print("\033[91m[!]Invalid option\n\033[91m")
                        dmpp
                    dmpp()
                dmpp()

            elif module == "help":
                modulesForDownt()

            elif module == "exit":
                sys.exit(exit_msg)
            
            elif module == "back":
                Guest()
            
            elif module == "home":
                main()
            else:
                print(f"\033[91m[!]'{module}' module not found\033[91m")

            downt()

        downt()
    elif module == "chgt":
        target = input("\033[92m[+]Enter new target::\033[92m")
        Guest()
    else:
        print(f"\033[91m[!]'{module}' module not found\033[91m")
        Guest()
        
# _____________________________________________________________________________________________________
# _____________________________________________________________________________________________________
# _____________________________________________________________________________________________________
# _____________________________________________________________________________________________________
# _____________________________________________________________________________________________________
# _____________________________________________________________________________________________________

def modulesForGuest():
    time.sleep(.5)
    table_datas = [
    ["\n\033[94m\033[136m\n\n\n\n\n\nMODULES\n", """
    downt               :  Download anything from profile.

    chgt                :  Change target.

    help                :  Display this help message.

    exit                :  Close Instrabot.\n\033[1;m\033[94m"""]
    ]
    table = DoubleTable(table_datas)
    print(table.table)        

def modulesForLogin():
    time.sleep(.5)
    table_datas = [
    ["\033[94m\033[136m\n\n\n\n\n\n\n\nMODULES\n", """
    downp               :  Download anything from profile.

    gfls                :  Get following and followers list.

    nfbi                :  list out all non-followback id's.

    ghostf              :  List out all Ghost Followers.

    fllw                :  Follow a id or id's 

    ufllw               :  Unfollow a id or id's.

    scf                 :  Search a user from someone else following or follower.

    adcm                :  An advanced comparison between two id.

    help                :  Display this help message.

    rmlog               :  Delete all login logs.

    exit                :  Close Instrabot.\n\033[1;m\033[94m"""]
    ]
    table = DoubleTable(table_datas)
    print(table.table)        

def modulesForDownp():
    time.sleep(.5)
    table_datas = [
    ["\033[94m\033[136m\n\n\n\n\n\n\n\n\n\n\n\nMODULES\n", """
    df                  :  Download every thing from profile with caption and tags.

    dpp                 :  Download profile pic.

    dmrp                :  Download the most recent post.

    dap                 :  Download all pic.

    dmpp                :  Download the most liked post

    tap                 :  Download a posts where the profile is tagged.

    hap                 :  Download the highlights of that profile.

    vap                 :  Download all videos from profile.

    gap                 :  Download all igtv videos from profile.+

    sap                 :  Download all saved from profile.+

    app                 :  Download a particular post.

    fap                 :  Download pictures from feed.

    uap                 :  Update a profile.

    help                :  Display this help message.

    exit                :  Close Instrabot.\n\033[1;m\033[94m"""]
    ]
    table = DoubleTable(table_datas)
    print(table.table)        

def modulesForDownt():
    time.sleep(.5)
    table_datas = [
    ["\033[94m\033[136m\n\n\n\n\n\n\n\n\n\n\n\nMODULES\n", """
    df                  :  Download every thing from profile with caption and tags.

    dpp                 :  Download profile pic.

    dmrp                :  Download the most recent post.

    dap                 :  Download all pic.

    dmpp                :  Download the most liked post

    tap                 :  Download a posts where the profile is tagged.

    vap                 :  Download all videos from profile.

    gap                 :  Download all igtv videos from profile.+

    app                 :  Download a particular post.

    uap                 :  Update a profile.

    help                :  Display this help message.

    exit                :  Close Instrabot.\n\033[1;m\033[94m"""]
    ]
    table = DoubleTable(table_datas)
    print(table.table)        

if __name__ == "__main__":
    main()