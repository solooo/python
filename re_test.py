
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
'''

pattern = re.compile('')
s = pattern.match(html)
type(s)
