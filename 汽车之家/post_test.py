from urllib import request, error, parse, robotparser
import ssl


def getdata(city):
    parmas = {
        'city': city,
        'needAddtionalResult': 'false'
    }
    # 1.字典转换成字符串，2.编码格式
    parmas = parse.urlencode(parmas, encoding='utf8')

    # 表单数据
    form_data = {
        'first': 'True',
        'kd': 'python',
        'pn': 1
    }
    # 1.转成url编码格式2.转换成字节类型
    form_data = parse.urlencode(form_data).encode('utf8')

    url_full = 'https://www.lagou.com/jobs/positionAjax.json?' + parmas
    # 请求头优先级，一般写前三个就可以了
    # 构造headers参数的权重
    # User-Agent:模拟浏览器登录
    # Cookie:保存用户信息,为了跟服务器的session保持一致
    # Referer:表示你当前的请求是从哪个页面或者说哪个接口跳转过来的
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'Cookie': 'WEBTJ-ID=07052018%2C102332-164684075381a3-07ec0d8ec2b4f38-7c2d6751-1049088-164684075396e; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1530757413,1530757450,1530757484; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1530757484; _ga=GA1.2.1612395762.1530757416; _gid=GA1.2.915355587.1530757416; user_trace_token=20180705102342-6fba2eec-7ffa-11e8-be76-525400f775ce; LGSID=20180705102342-6fba3232-7ffa-11e8-be76-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.汽车之家.com; PRE_SITE=https%3A%2F%2Fwww.汽车之家.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D1%26rsv_idx%3D1%26tn%3Dbaidu%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26oq%3D%2525E5%252595%2525A4%2525E9%252585%252592%2525E8%25258A%252582%26rsv_pq%3De1db13b40004a64e%26rsv_t%3D1c69cGCLUrbMW4Ztkq1SNoqpEMoPLe4ium8%252B5u6JQZ5VXWWKHlr6H%252B07nHo%26rqlang%3Dcn%26rsv_enter%3D0%26rsv_sug3%3D29%26rsv_sug1%3D5%26rsv_sug7%3D100%26rsv_sug4%3D703; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; LGRID=20180705102409-7fcd071d-7ffa-11e8-be76-525400f775ce; LGUID=20180705102342-6fba34e1-7ffa-11e8-be76-525400f775ce; _gat=1; JSESSIONID=ABAAABAACEBACDG3FAD2ECBEE6D0742EA0923CE7DD8A473; index_location_city=%E5%8C%97%E4%BA%AC; TG-TRACK-CODE=index_search; SEARCH_ID=97f31306c77c464db4c0ed2070944bd9',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
    }
    # 构造请求
    req = request.Request(url_full, headers=headers, data=form_data)
    context = ssl._create_unverified_context()
    response = request.urlopen(req, context=context)
    content = response.read().decode('utf8')
    print(content)


def main():
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=北京&needAddtionalResult=false'
    city = input('请输入查询的城市')
    getdata(city)


if __name__ == '__main__':
    main()
