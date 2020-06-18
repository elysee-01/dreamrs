from website.models import SiteInfo, SocialAccount


def base_info(request):

    site_info = SiteInfo.objects.filter(status=True)
    social_account = SocialAccount.objects.filter(status=True)
    
    data = {
        'site_info': site_info.last,
        'social_account': social_account,
    }
    
    return data