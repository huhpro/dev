from django.shortcuts import render

from posts.models import Post, Get_common_info

def main_page(request):
    #post_list = Post.objects.order_by('-created_date')
    #Get_common_info_list = Get_common_info.lists.order_by('-created_date')
    Get_common_info_list = Get_common_info.lists.order_by('name')

    #return render(request, 'main.html', {'post_list': post_list})
    return render(request, 'main.html', {'Get_common_info_list': Get_common_info_list})
