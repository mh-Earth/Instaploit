import instaloader
from time import time
from terminaltables import AsciiTable,DoubleTable

instra = instaloader.Instaloader()
def comparisonID(id1,id2,usename):
    t1 = time()
    datatable = []
    # _________________________checking id if the id exists____________________
    profile = instaloader.Profile.from_username(instra.context,id1)
    profile = instaloader.Profile.from_username(instra.context,id2)
    # _____________________making data table_________________________
    Heading = ["Properties",id1,id2]
    username = ["Username"]
    fullName = ["Full Name"]
    userId = ["User-ID"]

    followers = ["Total Follower"]
    followees = ["Total Following"]

    avgComment = ["Average comment"]
    totalComment = ["Total Comment"]
    maxComment = ["Max comment in a post"]
    miniComment = ["Minimam comment in a post"]

    avgLike = ["Average like"]
    totalLike = ["Total like"]
    maxLike = ["Max like in a post"]
    miniLike = ["Minimam likes in a post"]

    instagramRate = ["Instagram active user rate"]
    Biography = ["Biography"]
    totalPost = ["Total post"]
    totalIgtvPost = ["Total Igtv videos"]
    totalTaggedPost = ["Total Tagged Post"]
    IsVerified = ["Profile Verified"]
    ExternalUrl = ["External Url"]
    isPrivate = ["Is Private"]
    businessCategoryName = ["Business category name"]
    hasBlockedViewer = ["Has Blocked Viewer"]
    instra.load_session_from_file(usename)
    Biography = []


#  ____________________________Gathering information for id1_________________________________

    profile = instaloader.Profile.from_username(instra.context,id1)
    print(f"\033[92m[+]Gathering information in 3 Step for {id1} please wait........\033[92m")

    totalComments = 0
    totalLikes = 0
    maxLikes = 0
    maxComments = 0
    miniLikes = 100000000000000
    miniComments = 10000000000000
    for post in profile.get_posts():
        totalComments += post.comments
        totalLikes += post.likes

        if post.likes>maxLikes:
            maxLikes = post.likes

        if post.comments>maxComments:
            maxComments = post.comments
        
        if post.likes<miniLikes:
            miniLikes = post.likes
        
        if post.comments<miniLikes:
            miniComments = post.comments
        
            

    totalPosts = profile.get_posts().count

    print(f"\033[92m[+]Step 1 done for {id1}\033[92m")

    avgLikes = int(totalLikes/totalPosts)
    avgComments = int(totalComments/totalPosts)

    instagramRates = (totalLikes+totalComments)/profile.get_followers().count*100
    print(f"\033[92m[+]Step 2 done for {id1}\033[92m")

#  ____________________________adding id1 information in datatable_________________________________

    username.append(profile.username)
    fullName.append(profile.full_name)
    followers.append(profile.get_followers().count)
    followees.append(profile.get_followees().count)
    totalTaggedPost.append(profile.get_tagged_posts().count)
    totalPost.append(totalPosts)
    totalIgtvPost.append(profile.get_igtv_posts().count)
    IsVerified.append(profile.is_verified)
    userId.append(profile.userid)
    ExternalUrl.append(profile.external_url)
    isPrivate.append(profile.is_private)
    businessCategoryName.append(profile.business_category_name)
    hasBlockedViewer.append(profile.has_blocked_viewer)
    totalComment.append(totalComments)
    totalLike.append(totalLikes)
    avgComment.append(avgComments)
    avgLike.append(avgLikes)
    instagramRate.append(instagramRates)

    maxComment.append(maxComments)
    maxLike.append(maxLikes)

    miniLike.append(miniLikes)
    miniComment.append(miniComments)
    Biography.append(profile.biography)
    print(f"\033[92m[+]Step 3 done for {id1}\033[92m")


    
#  ____________________________Gathering information for id2_________________________________
    profile = instaloader.Profile.from_username(instra.context,id2)
    print(f"\033[92m[+]Gathering information in 3 Step for {id2} please wait........\033[92m")


    totalComments = 0
    totalLikes = 0
    maxLikes = 0
    maxComments = 0
    miniLikes = 100000000000000
    miniComments = 10000000000000
    for post in profile.get_posts():
        totalComments += post.comments
        totalLikes += post.likes

        if post.likes>maxLikes:
            maxLikes = post.likes
            postURL=post.url

        if post.comments>maxComments:
            maxComments = post.comments
        
        if post.likes<miniLikes:
            miniLikes = post.likes
        
        if post.comments<miniLikes:
            miniComments = post.comments
        
            

    totalPosts = profile.get_posts().count

    print(f"\033[92m[+]Step 1 done for {id2}\033[92m")

    avgLikes = int(totalLikes/totalPosts)
    avgComments = int(totalComments/totalPosts)

    instagramRates = (totalLikes+totalComments)/profile.get_followers().count*100
    print(f"\033[92m[+]Step 2 done for {id2}\033[92m")

#  ____________________________adding id2 information in datatable_________________________________
    username.append(profile.username)
    followers.append(profile.get_followers().count)
    followees.append(profile.get_followees().count)
    totalTaggedPost.append(profile.get_tagged_posts().count)
    fullName.append(profile.full_name)
    totalPost.append(totalPosts)
    Biography.append(profile.biography)
    totalIgtvPost.append(profile.get_igtv_posts().count)
    IsVerified.append(profile.is_verified)
    userId.append(profile.userid)
    ExternalUrl.append(profile.external_url)
    isPrivate.append(profile.is_private)
    businessCategoryName.append(profile.business_category_name)
    hasBlockedViewer.append(profile.has_blocked_viewer)
    totalComment.append(totalComments)
    totalLike.append(totalLikes)
    avgComment.append(avgComments)
    avgLike.append(avgLikes)
    instagramRate.append(instagramRates)

    maxComment.append(maxComments)
    maxLike.append(maxLikes)

    miniLike.append(miniLikes)
    miniComment.append(miniComments)
    print(f"\033[92m[+]Step 3 done for {id2}\033[92m")


#  ____________________________adding information in datatable_________________________________

    print(f"\033[92m[+]Listing all collected information....\n\033[92m")

    datatable.append(Heading)
    datatable.append(username)
    datatable.append(fullName)
    datatable.append(userId)
    datatable.append(followers)
    datatable.append(followees)

    datatable.append(totalPost)
    datatable.append(totalLike)
    datatable.append(totalComment)

    datatable.append(maxLike)
    datatable.append(miniLike)
    datatable.append(avgLike)

    datatable.append(maxComment)
    datatable.append(miniComment)
    datatable.append(avgComment)

    datatable.append(totalIgtvPost)
    datatable.append(totalTaggedPost)

    datatable.append(ExternalUrl)

    datatable.append(IsVerified)
    datatable.append(isPrivate)
    datatable.append(businessCategoryName)
    datatable.append(hasBlockedViewer)

    datatable.append(instagramRate)

    try:
        table = DoubleTable(datatable)
        print(table.table)
        print(f"\n{id1}:{Biography[0]}\n\n{id2}:{Biography[1]}\n")
        print(f"\033[92m[+]Saveing information as {id1}&{id2}.txt\033[92m")
        f = open(f"{id1}&{id2}.txt","w")
        f.write(table.table)
        f.write(f"\n{id1}:{Biography[0]}\n\n{id2}:{Biography[1]}")
        f.close()
    except Exception as e:
        print(f"\033[91m[-]{e}\033[91m")
    t2 = time()
    print(f"\033[92m[+]Finished in {t2-t1}s\033[92m")

comparisonID("_python_coding","intracoder","_python_coding")