'''
Author: Rongxin rongxin@u.nus.edu
Date: 2025-03-29 13:04:39
LastEditors: Rongxin rongxin@u.nus.edu
LastEditTime: 2025-03-30 03:23:08
FilePath: /wos-crawler/wos_crawler/wos_crawler/spiders/wos.py
'''
import json
from http.cookies import SimpleCookie

import scrapy
from rich import print as pp
from scrapy import Request, Spider
from scrapy.utils.project import get_project_settings
from scrapy_aiohttp import AiohttpRequest


class WosSpider(scrapy.Spider):
    name = "wos"
    # allowed_domains = ["www-webofscience-com.libproxy1.nus.edu.sg"]
    def start_requests(self):
        # use case: scrapy_aiohttp.AiohttpRequest

        settings=get_project_settings()
        url_base=settings['URL_BASE']
        rawdata=settings['COOKIES']
        cookies = SimpleCookie()
        cookies.load(rawdata)
        url=f"https://{url_base}/api/esti/SearchEngine/search"
        pp(f"[>>] The URL_BASE is {url_base}")
        # pp(f"[>>] The COOKIES is {settings['COOKIES']}")
        # pp(f"[>>] The start_urls is {start_urls[0]}")
        
        data=b"{\"search\":{\"mode\":\"author_id\",\"database\":\"AUTHOR\",\"authorId\":{\"type\":\"spid\",\"value\":\"10414390,1039682,1854264,5212608,564204,779628\"}},\"retrieve\":{\"Count\":6,\"FirstRecord\":1,\"Options\":{\"View\":\"AuthorIds\",\"DataFormat\":\"Map\",\"ReturnType\":\"List\",\"RemoveQuery\":\"On\"}}}"
    

        # Even though SimpleCookie is dictionary-like, it internally uses a Morsel object
        # which is incompatible with requests. Manually construct a dictionary instead.
        cookies = {k: v.value for k, v in cookies.items()}
        yield AiohttpRequest(
            url=url,
            method="POST",
            cookies=cookies,
            body=data,
            callback=self.parse
        )
        

    def parse(self, response, **kwargs):
        pp(f"[>>] The response is {response.text}")
        return {"url": response.url}