import requests

api_dev_key 			= 'cf939ac028875113b2ab1286ea653994' # your api_developer_key
api_paste_code 		= '''
#include <stdio.h>

typedef  struct struAVClass{
    const char* class_name;
    const char* (*item_name)(void* ctx);
    const char* option;
}AVClass;


#define DEFINE_WRITER_CLASS(name)                   \\
static const char *name##_get_name(void *ctx)       \\
{                                                   \\
    return #name ;                                  \\
}                                                   \\
static const AVClass name##_class = {               \\
    .class_name = #name,                            \\
    .item_name  = name##_get_name,                  \\
    .option     = "name##_options"                  \\
}

static const char* test_options = "test_options";
static const char* west_options = "west_options";
DEFINE_WRITER_CLASS(test);
DEFINE_WRITER_CLASS(west);

int main()
{
    printf("class_name=%s, item_name=%s, option=%s\n", test_class.class_name, test_class.item_name(NULL), test_class.option);
    printf("class_name=%s, item_name=%s, option=%s\n", west_class.class_name, west_class.item_name(NULL), west_class.option);
    return 0;
}
'''
 #your paste text
api_paste_private 		= '0' #0=public 1=unlisted 2=private
api_paste_name			= 'c语言#/##的使用' #name or title of your paste
api_paste_expire_date 		= '10M'
api_paste_format 		= 'c'
api_user_key 			= '4282bf4837e7b8bc1ddfd3f061111b62' #if an invalid or expired api_user_key is used, an error will spawn. If no api_user_key is used, a guest paste will be created


url 				= 'https://pastebin.com/api/api_post.php'

API_OPTIONS = {'TREND': 'trends',
               'PASTE': 'paste',
               'USER_PASTE': 'list',
               'DELETE_PASTE': 'delete',
               'USER_RAW_PASTE': 'show_paste'}

data = {
    "api_dev_key": api_dev_key,
    "api_user_key": api_user_key,
    "api_paste_code": api_paste_code,
    "api_paste_private": api_paste_private,
    "api_paste_name": api_paste_name,
    "api_paste_format": api_paste_format,
    "api_option": API_OPTIONS["PASTE"],
}

r = requests.post(url, data, {"verify": False})
print(r.text)

