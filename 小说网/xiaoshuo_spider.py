from urllib import request, error
import ssl
import re
import os


def send_request(url, charset_code='utf-8', is_decode=True):
    '''封装一个函数来发起请求,需要传入目标url和网页编码,返回响应体内容'''

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0',
        # 'Host': 'www.readnovel.com',
        # 'Cookie': '_csrfToken=XS39HDWBVWvPMw1aXK5wmhwXCAfXZgHcTaSF68r0; newstatisticUUID=1530781894_1297669144'
    }

    req = request.Request(url, headers=headers)
    response = request.urlopen(req, context=ssl._create_unverified_context())
    if is_decode:
        result = response.read().decode(charset_code)
    else:
        result = response.read()
    return result


def image_load(result, filename):
    '''把二进制字节流写入文件,request表示字节流,filename表示文件名'''
    with open(filename, 'wb') as f:
        f.write(result)


def txt_load(result, filename, dirname):
    '''把一些文本内容写进文件'''
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    with open(filename, 'w') as f:
        f.write(result)


def main():
    # 第一页的url
    for page in range(1, 2):
        url = 'https://www.readnovel.com/rank/hotsales?pageNum=' + str(page)
        # 图片格式.JPEG
        #
        img_str = '<div class="book-img-box"><span class="rank-tag no1">1</span><a href="//www.readnovel.com/book/9500446903583303" target="_blank" data-eid="qd_C39" data-bid="9500446903583303"><img src="//qidian.qpic.cn/qdbimg/349573/c_9500446903583303/150"></a></div>'
        content_str = '<div class="book-mid-info"><h4><a href="/book/9500446903583303" target="_blank" data-eid="qd_C40" data-bid="9500446903583303">暖婚似火：顾少，轻轻宠</a></h4><p class="author"><img src="//qidian.gtimg.com/readnovel/images/ico/account.1e031.png"><a class="name default" href="javascript:" target="_blank" data-eid="qd_C41">芊霓裳</a><em>|</em><a href="/all/?catId=30020" target="_blank" data-eid="qd_C42">现代言情</a><em>|</em><span>连载中</span></p><p class="intro">“顾先生，不要，你太大了…”“年纪大的男人会疼女人。”未婚夫背叛，唐沫儿一不小心招惹上了京都豪门贵胄顾墨寒，并陷入了他的情网，后来她才知道他只是想让她生一个继承人。三年后，一个小奶包跑过来抱住了她的大腿，“给我买根棒棒糖，我把我爹地送给你哦。”英俊挺拔的男人将她抵在墙角里，她一脸的茫然，“先生，你是谁？”“乖，宝贝儿，这一次我一定轻轻宠。”（1v1，娱乐圈打脸爽文+宠文，亿万第二部）</p><p class="update"><a href="/chapter/9500446903583303/29517089266104674" target="_blank" data-eid="qd_C43" data-bid="9500446903583303" data-cid="">最新更新 第682章 璇玑苏醒，陆林cp倒计时（16）</a><em>·</em><span>17小时前</span></p></div>'
        #
        pattern = re.compile(
            '.*?book-img-box.*?href="(.*?)".*?data-bid.*?src="(.*?)".*?data-bid.*?>(.*?)</a>.*?name.*?data-eid.*?>(.*?)</a>.*?intro">(.*?)</p>.*?update.*?data-cid.*?>(.*?)</a>.*?<span>(.*?)</span>',
            re.S)
        result = send_request(url)
        result = re.findall(pattern, result)

        for item in result:

            imageurl = 'https:' + item[1]
            # 文件夹名字
            dirname = item[2]
            # 图片名字
            imagename = dirname + '/' + item[2].replace('/', '') + '.jpeg'
            # txt文件名字
            filename = dirname + '/' + item[2].replace('/', '') + '.txt'
            result = ''
            for i in item:
                result = result + i + '\n'
            txt_load(result, filename, dirname)
            try:
                img_result = send_request(imageurl, is_decode=False)
                image_load(img_result, imagename)
            except error.HTTPError as e:
                print(e.reason)
            except error.URLError as e:
                print(e.reason)
            else:
                pass

            # 详情页的URL，加上一个锚点，就是就能返回带有目录的html
            detail_url = 'https:' + item[0] + '#Catalog'
            # print(detail_url)
            # 请求目录页,得到目录页的html文件
            result = send_request(detail_url)
            # 使用正则匹配到免费章节

            detail_pattern = re.compile('.*?rid.*?href="(.*?chapter.*?)".*?a>', re.S)
            result = re.findall(detail_pattern, result)
            print((len(result)))

if __name__ == '__main__':
    main()
