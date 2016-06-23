
import re

html = '''
{
                                "thumbURL":"http://img1.imgtn.bdimg.com/it/u=4272798765,523948214&fm=21&gp=0.jpg",
                                "middleURL":"http://img1.imgtn.bdimg.com/it/u=4272798765,523948214&fm=21&gp=0.jpg",
                                "largeTnImageUrl":"",
                                "hasLarge" : true,// 0,
                                "hoverURL":"http://img1.imgtn.bdimg.com/it/u=4272798765,523948214&fm=23&gp=0.jpg",
                                "pageNum":19,
                                "objURL":"http://a.hiphotos.baidu.com/zhidao/pic/item/0ff41bd5ad6eddc4f995afa438dbb6fd5266337a.jpg",
                                "fromURL":"http://zhidao.baidu.com/question/547157576.html",
"os":"746439172,4060812556",
                                "simid":"3438721281,300189250",
                                "pi":"0",
                                "adType":"0",
                                "setDowloadURL":"",
                                "setTittle":"",
                                "DecorateCompanyName":"",
                                "DecorateCompanyLocation":"",
                                "DecorateWantuUrl":"",
                                "personalized":"0"
                }
                ,                                {
                                "thumbURL":"http://img5.imgtn.bdimg.com/it/u=99980900,631435245&fm=21&gp=0.jpg",
                                "middleURL":"http://img5.imgtn.bdimg.com/it/u=99980900,631435245&fm=21&gp=0.jpg",
                                "largeTnImageUrl":"",
                                "hasLarge" : true,// 0,
                                "hoverURL":"http://img5.imgtn.bdimg.com/it/u=99980900,631435245&fm=23&gp=0.jpg",
                                "pageNum":27,
                                "objURL":"http://www.deskcar.com/desktop/else/20101022103026/8.jpg",
                                "fromURL":"http://www.deskcar.com/html/6346/8.shtml",
                                "fromURLHost":"www.deskcar.com",
                                "currentIndex":"",
                                "width":1280,
                                "height":1024,
                                "type":"jpg",
                                "filesize":"",
'''

pattern = re.compile(r'"middleURL":"(http://.+)"')
s = pattern.findall(html)
if s:
    print(s)
