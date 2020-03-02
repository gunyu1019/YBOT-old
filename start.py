import discord
import asyncio
import requests
import random
import os
import sys
import urllib
import time

from discord.ext import commands

def log_info(channel, user, message):
    Ftime = time.strftime('%Y-%m-%d %p %I:%M:%S', time.localtime(time.time()))
    print("[시간: " + str(Ftime) + ",채널: " + str(channel) + ",유저: " + str(user) + "]: " + str(message))
    log = open("log.txt","a")
    log.write("[시간: " + str(Ftime) + ",채널: " + str(channel) + ",유저: " + str(user) + "]: " + str(message) + "\n")
    log.close()
    #log_info(message.channel,message.author,message.content)
    
log_info('로컬(Ybot)','로컬(Ybot)','디스코드 계정로그인중입니다.')
client = discord.Client()
    
@client.event
async def on_ready():
    log_info('로컬(Ybot)','로컬(Ybot)','디스코드 봇 로그인이 완료되었습니다.')
    log_info('로컬(Ybot)','로컬(Ybot)',client.user.name)
    log_info('로컬(Ybot)','로컬(Ybot)',client.user.id)
    print('------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("=help 를 이용하여, 명령어를 알아보세요!"))

@client.event
async def on_message(message):
    list_message = message.content.split(' ')
    if message.author == client.user:
        return
    if message.content.startswith('=help'):
        
        log_info(message.channel,message.author,message.content)
        #embed = discord.Embed(title="Ybot helper", description='**=코로나**: 코로나 정보를 알려줍니다.\n아직 업그레이드 중이에요. 양해부탁드립니다 ㅎㅎ\n**=주사위**: 주사위 두개를 굴려줍니다.\n**=한강 수온**: 한강수온을 확인해줍니다.\n**=날씨**: 날씨정보를 알려줍니다.\n**=번역**: 번역해줍니다.', color=0x00aaaa)
        #embed.add_field(name="=", value="신분당선", inline=False)
        embed = discord.Embed(title="Ybot helper", color=0x00aaaa)
        embed.add_field(name="=코로나 [지역(선택)]", value="실시간 코로나 정보를 알려줍니다.\n지역목록: 서울,부산,대구,인천,광주,대전,울산,세종,경기,강원,충북,충남,전북,전남,경북,경남,제주", inline=False)
        embed.add_field(name="=코로나해외 [대륙]", value="실시간 코로나 정보를 알려줍니다.\n지역목록: 아시아,유럽,중동,아메리카,오세아니아,아프리카,기타", inline=False)
        embed.add_field(name="=주사위", value="두개의 주사위를 굴립니다.", inline=False)
        embed.add_field(name="=한강 수온", value="한강 수온을 알려줍니다.", inline=False)
        embed.add_field(name="=날씨 [지역 혹은 '전국']", value="날씨를 알려줍니다. 날씨기능은 오타가 나도 자동적으로 고쳐서 알려주며, 해외 날씨도 확인할수 있습니다.", inline=False)
        embed.add_field(name="=실시간 검색어", value="네이버 급상승 실시간 검색어 TOP20을 불러옵니다.", inline=False)
        embed.add_field(name="=택배 [운송장번호] [택배회사(선택)] 혹은 =택배 목록", value="택배 배송현황을 추적하여 알려줍니다. 택배회사를 기재하지 않아도, 자동적으로 찾아줍니다.\n(일부 회사는 자동추적이 불가능합니다. 또한, 일 20회로 제한합니다.)", inline=False)
        embed.add_field(name="=번역 [번역할 언어] [내용]", value="[내용]을 번역해줍니다. 시작할 언어는 알아서 분석하여 설정합니다.\n언어는 한국어,영어,일본어,중국어(간체/번체),스페인어,프랑스어,러시아어,베트남어,인도네시아어,태국어,독일어,이탈리아어를 지원합니다.\n(다소 일부언어간은 상호작용이 안될수 있습니다.)", inline=False)
        embed.add_field(name="=재난문자 [로딩할 갯수(선택)] [지역 혹은 전국(선택)]", value="재난 문자를 불러옵니다. 선택을 미기재시 10개, 전국으로 설정됩니다.\n지역은 (도/시)만 가능합니다.", inline=False)
        embed.add_field(name="=스팀 [ID 혹은 유저코드] [유저코드 활성화여부]", value="Steam 프로필파일을 불러옵니다.\nID가 안될경우, 유저코드를 이용해보시기 바라며, 유저코드를 사용시에는 유저코드 활성화여부에다가 아무내용(빈공간 존재시 불가능)을 작성하시면 됩니다.", inline=False)
        embed.add_field(name="=PUBG [닉네임] [시즌(선택)]", value="배틀그라운드 전적을 검색해줍니다.", inline=False)
        embed.add_field(name="=청소 [갯수]", value="갯수만큼 내용을 지웁니다.\n 해당기능을 사용시에는 메세지 관리하기 기능을 주셔야지만 가능합니다.", inline=False)
        embed.add_field(name="=사용자문제", value="말그대로 사용자문제", inline=False)
        embed.add_field(name="=레인보우식스 [닉네임]", value="레인보우식스 전적을 검색해줍니다.", inline=False)
        embed.add_field(name="=오버워치 [닉네임] [빠른대전/경쟁전]", value="오버워치 전적을 검색해줍니다.", inline=False)
        embed.add_field(name="=따라하기 [내용]", value="그 내용을 따라해줍니다.", inline=False)
        embed.set_footer(text="용현봇 v3.0(powered by python3)")
        await message.channel.send(embed=embed)
        return
    if message.content.startswith('=코로나해외'):
        log_info(message.channel,message.author,message.content)
        world_list = ["아시아","유럽","중동","아메리카","오세아니아","아프리카","기타"]
        try:
            false_data = list_message[1]
        except:
            embed = discord.Embed(title="Ybot helper",description="=코로나해외 [대륙]\n지역목록: 아시아,유럽,중동,아메리카,오세아니아,아프리카,기타", color=0xffa500)
            await message.channel.send(embed=embed)
            return
        else:
            world = list_message[1]
        embed = discord.Embed(title="해외 코로나바이러스감염증-19의 현황", url="http://ncov.mohw.go.kr/index_main.jsp", color=0xffa500)
        html1 = requests.get("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=").text
        html2 = html1.split('<tbody>')[2].split('</tbody>')[0]
        html2_list = html2.split('scope="row">')
        html3 = ''
        for i in range(len(world_list)-1):
            if html2.split('scope="row">')[i+1].split('</th>')[0] == world:
                html3 = html2.split('</th>')[i+1].split('<th')[0]
        if html3 == '':
            embed = discord.Embed(title="Ybot helper",description="아직 확진자가 없거나, 아래의 대륙만 지원합니다.\n지역목록: 아시아,유럽,중동,아메리카,오세아니아,아프리카", color=0xffa500)
            await message.channel.send(embed=embed)
            return
        list_count = len(html3.split('<td>')) -1
        for i in range(list_count):
            area = html3.split('<td class="w_bold">')[i+1].split('</td>')[0]
            area_count = html3.split('<td>')[i+1].split('</td>')[0]
            embed.add_field(name=area, value=area_count, inline=True)
            if area == "일본":
                area_count = html2.split('<td class="w_bold">일본 크루즈</td>')[1].split('</td>')[0].replace('<td>','',1)
                embed.add_field(name="일본 크루즈", value=area_count, inline=True)
        #URL_picture = html1.split('<img alt="" src="')[1].split('" />')[0]
        #embed.set_image(url="http://ncov.mohw.go.kr" + URL_picture)
        #embed.set_footer(text="사진출처: 질병관리본부")
        embed.add_field(name="해외종합: ", value=html2.split('<td class="w_bold">')[len(html2.split('<td class="w_bold">'))-1].split('</td>')[0], inline=True)
        await message.channel.send(embed=embed)
        return
    if message.content.startswith('=코로나'):
        log_info(message.channel,message.author,message.content)
        html = requests.get("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=").text
        data_count = 1
        try:
            data_false1 = list_message[1]
        except:
            local_search = "전국"
        else:
            local_search = list_message[1]
            total_count = html.split('td headers="status_con s_type1" class="number"')
        if local_search == "전국":
            data_count = 1
        elif local_search == "검역대":
            data_count = len(total_count)-1
        else:
            for i in range(len(total_count)-2):
                if local_search == html.split('<th scope="row">')[i+1].split('</th>')[0]:
                    data_count = i+1
                    break
                elif len(total_count)-2 == i and data_count == 1:
                    embed = discord.Embed(title="Ybot helper", description='지역목록: 서울,부산,대구,인천,광주,대전,울산,세종,경기,강원,충북,충남,전북,전남,경북,경남,제주', color=0x00aaaa)
        Increased = html.split('<td class="number">')[(data_count * 2) - 1].split('</td>')[0]
        Confirmator = html.split('<td headers="status_con s_type2" class="number">')[data_count].split('</td>')[0]
        Healer = html.split('<td headers="status_con s_type3" class="number">')[data_count].split('</td>')[0]
        Dead = html.split('<td headers="status_con s_type4" class="number">')[data_count].split('</td>')[0]
        Inspection = html.split('<td headers="status_test s_type6" class="number">')[data_count].split('</td>')[0]
        Negative = html.split('<td headers="status_test s_type7" class="number">')[data_count].split('</td>')[0]
        Total = html.split('<td class="number">')[data_count * 2].split('</td>')[0]
        LastUpdate = html.split('<p class="info"><span>')[1].split('</span>')[0]
        #embed = discord.Embed(title="신종코로나 확진자수", description=" 확진환자: "  + Confirmator + "\n 완치자: " + Healer + "\n 사망자: " + Dead + "\n 검사진행: " + Inspection + "\n 최근 업데이트: " + LastUpdate, color=0xffa500)
        embed = discord.Embed(title=local_search + "지역의 코로나바이러스감염증-19의 현황", url="http://ncov.mohw.go.kr/index_main.jsp", color=0xffa500)
        embed.add_field(name="확진환자", value=Confirmator + "명(+" + Increased + "명)", inline=True)
        embed.add_field(name="완치(격리해제)", value=Healer + "명", inline=True)
        embed.add_field(name="사망자", value=Dead + "명", inline=True)
        embed.add_field(name="검사진행", value=Inspection + "명", inline=True)
        embed.add_field(name="음성판정", value=Negative + "명", inline=True)
        embed.add_field(name="종합", value=Total + "명", inline=True)
        embed.set_footer(text="최근 업데이트: " + LastUpdate + " 기준")
        await message.channel.send(embed=embed)
        return
    if message.content.startswith('=주사위'):
        log_info(message.channel,message.author,message.content)
        dice_imoji = ':one:' ,':two:',':three:',':four:',':five:',':six:'
        embed = discord.Embed(title="주사위!~", description='주사위를 돌립니다!', color=0x00aaaa)
        first_dice =  random.choice(dice_imoji)
        msg = await message.channel.send(embed=embed)
        await asyncio.sleep(3.0)
        await msg.delete()
        twice_dice =  random.choice(dice_imoji)
        #embed = discord.Embed(title="두둥탁", description='첫 번째로 돌린 주사위 값은?' + first_dice + '\n두 번째로 돌린 주사위 값은?'  + twice_dice, color=0x00aaaa)
        embed = discord.Embed(title="두둥탁", color=0x00aaaa)
        embed.add_field(name="첫 번째로 굴린 주사위 값은?", value=first_dice, inline=False)
        embed.add_field(name="두 번째로 굴린 주사위 값은?", value=twice_dice, inline=False)
        await message.channel.send(embed=embed)
        return
    if message.content.startswith('=한강 수온'):
        log_info(message.channel,message.author,message.content)
        html = requests.get("https://www.wpws.kr/hangang/").text
        water_temp = html.split('<p id="temp"><i class="xi-tint"></i>')[1].split('</p>')[0]
        embed = discord.Embed(title="한강수온", description='한강의 수온은 약 ' + water_temp + ' 입니다.\n 설마? 이 온도라고 한강에서 수영하실려는건 아니겠죠?', color=0x00aaaa)
        await message.channel.send(embed=embed)
        return
    if message.content.startswith('=날씨'):
        log_info(message.channel,message.author,message.content)
        if message.content.replace("=날씨",'',1)=='' or message.content.replace("=날씨",'',1)==' ':
            embed = discord.Embed(title='Ybot helper', description='날씨는 다음과 같이 사용할수 잇습니다.\n=날씨 전국: 전국 날씨를 요약해서 보여줍니다.\n=날씨 (지역): 해당 지역의 날씨를 자세히 보여줍니다.', color=0x00aaaa)
            await message.channel.send(embed=embed)
            return
        elif list_message[1] == '전국':
            html = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%A0%84%EA%B5%AD%EB%82%A0%EC%94%A8").text
            local = html.split('<span>')
            data = html.split('<span class="state state4">')
            data_temp = html.split('<span class="dsc">')
            data_answer = ""
            for i in range(12):
                data_answer = data_answer + local[22+i].split('</span>')[0] + "지역 | 온도: " + data_temp[1+i].split('</span>')[0] +  "도\n"
            embed = discord.Embed(title="전국 날씨", description=data_answer, color=0x00aaaa)
            await message.channel.send(embed=embed)
        else:
            try:
                search_local = message.content.replace("=날씨 ","",1)
                html = requests.get("http://search.naver.com/search.naver?query=" + search_local + " 날씨").text
                title_weather = html.split('<h3 class="api_title">')[1].split('</h3>')[0]
                try:
                    data_false = html.split('오존지수</a>')[1]
                except:
                    status_weather = html.split('<p class="cast_txt">')[1].split(', ')[0]
                    today_temp = html.split('<span class="todaytemp">')[1].split('</span>')[0]
                    data1 = html.split('체감온도')[1].split('</p>')[0]
                    data2 = html.split('<span class="num">')[1].split('</span>')[0]
                    data3 = html.split('<span class="num">')[2].split('</span>')[0]
                    data4 = html.split('<span class="num">')[3].replace('<',')',1).split('/span>')[0].replace(' ','(',1)
                    embed = discord.Embed(title=title_weather, description='날씨 상태: ' + status_weather +'\n현재온도: ' + today_temp + '℃\n체감온도: ' + data1 + '\n바람: ' + data2 + 'm/s\n습도: ' + data3 + '%\n자외선: ' + data4, color=0x00aaaa)
                    #data2 = data3= data5 = data6 = data7 = "미지원(확인 불가능"
                else:
                    status_weather = html.split('<p class="cast_txt">')[1].split('</p>')[0]
                    today_temp = html.split('<span class="todaytemp">')[1].split('</span>')[0]
                    data1 = html.split('<span class="num">')[1].split('</span>')[0]
                    data2 = html.split('<span class="num">')[2].split('</span>')[0]
                    data3 = html.split('<span class="num">')[3].split('</span>')[0]
                    data4 = html.split('<span class="num">')[4].split('</span>')[0]
                    data5 = html.split('<span class="num">')[5].replace('</span>','(',1).split('<span')[0]
                    data6 = html.split('<span class="num">')[6].replace('</span>','(',1).split('<span')[0]
                    data7 = html.split('<span class="num">')[7].replace('</span>','(',1).split('<span')[0]
                    embed = discord.Embed(title=title_weather, description=status_weather +'\n현재온도: ' + today_temp +'℃(' + data1 + '℃/' + data2 + '℃)\n체감온도: ' + data3 + '℃\n시간당 강수량: ' + data4 + '\n미세먼지: ' + data5 + ')\n초미세먼지: ' + data6 + ')\n오존: ' + data7 + ')', color=0x00aaaa)
                await message.channel.send(embed=embed)
            except:
                embed = discord.Embed(title='에러', description='해당 지역이 존재하지 않습니다. 다시 확인후 입력해 주시기 바랍니다.', color=0x00aaaa)
                await message.channel.send(embed=embed)
        return
    if message.content.startswith('=실시간 검색어'):
        log_info(message.channel,message.author,message.content)
        html = requests.get("https://m.search.naver.com/search.naver?query=%EC%8B%A4%EC%8B%9C%EA%B0%84%20%EA%B2%80%EC%83%89%EC%96%B4").text
        data = html.split('span class="tit _keyword">')
        answer = ''
        embed = discord.Embed(title='[네이버 실시간 검색어 순위]', color=0x00aa00)
        for i in range(20):
            data_cache = data[i+1].split('</span>')[0]
            answer = answer + str(i+1) + '위: ' + data_cache + '\n'
        embed = discord.Embed(title='[네이버 실시간 검색어 순위]', description=answer, color=0x00aa00)
        await message.channel.send(embed=embed)
        return
    if message.content.startswith('=번역'):
        log_info(message.channel,message.author,message.content)
        try:
            data_false = list_message[2]
        except:
            embed = discord.Embed(title='Ybot helper', description='=번역 (번역할 언어) (번역할 단어) 위와같이 적어주셔야 작동합니다. (시작된 언어는 자동으로 추적합니다.)', color=0x00aaaa)
            await message.channel.send(embed=embed)
            return
        else:
            try:
                client_id = "5GsssVzuZ_jZ2HaOJ6TK"
                client_secret = "u9jjDNZ516"
                end_language = list_message[1]
                text = message.content.replace('=번역 ' + end_language + ' ',' ',1) #분별작업
                end_language_data = ['ko','en','ja','zh-CN','zh-TW','es','fr','ru','vi','th','id','de','it']
                chk_language_data = ['한국어','영어','일본어','중국어-간체','중국어-번체','스페인어','프랑스어','러시아어','베트남어','태국어','인도네시아어','독일어','이탈리아어']
                Fend_language = None
                for i in range(len(end_language_data)):
                    if end_language == chk_language_data[i]:
                        Fend_language = end_language_data[i]
                        break
                if Fend_language == None:
                    embed = discord.Embed(title='에러', description='존재하지 않는 단어입니다.\n용현봇은 위 13가지 언어만 지원합니다.\n\n[지원하는 단어]\n한국어,영어,일본어,중국어-간체,중국어-번체,스페인어,프랑스어,러시아어,베트남어,인도네시아어,태국어,독일어,이탈리아어', color=0x00aaaa)
                    await message.channel.send(embed=embed)
                    return #끝 언어 설정
                encQuery = urllib.parse.quote(text)
                data = "query=" + encQuery
                url = "https://openapi.naver.com/v1/papago/detectLangs"
                request = urllib.request.Request(url)
                request.add_header("X-Naver-Client-Id",client_id)
                request.add_header("X-Naver-Client-Secret",client_secret)
                response = urllib.request.urlopen(request, data=data.encode("utf-8"))
                rescode = response.getcode()
                if(rescode==200):
                    response_body = response.read()
                    start_language = response_body.decode('utf-8').replace('{"langCode":"','',1).replace('"}','',1)
                else:
                    embed = discord.Embed(title='에러', description="Error Code:" + rescode, color=0x00aaaa)
                    await message.channel.send(embed=embed)
                    return#시작 언어 설정
                encText = urllib.parse.quote(text)
                data = "source=" + start_language + "&target=" + Fend_language + "&text=" + encText
                url = "https://openapi.naver.com/v1/papago/n2mt"
                request = urllib.request.Request(url)
                request.add_header("X-Naver-Client-Id",client_id)
                request.add_header("X-Naver-Client-Secret",client_secret)
                response = urllib.request.urlopen(request, data=data.encode("utf-8"))
                rescode = response.getcode()
                if(rescode==200):
                    response_body = response.read()
                    embed = discord.Embed(title='번역 결과!', description=response_body.decode('utf-8').split('"translatedText":"')[1].replace('"}}}','',1), color=0x00aaaa)
                else:
                    embed = discord.Embed(title='에러', description="Error Code:" + rescode, color=0x00aaaa)
                await message.channel.send(embed=embed)
            except:
                embed = discord.Embed(title='에러', description="번역에 실패하였습니다.", color=0x00aaaa)
                await message.channel.send(embed=embed)
        return
    if message.content.startswith('=택배'):
        log_info(message.channel,message.author,message.content)
        try:
            try:
                data_false = list_message[1]
            except:
                embed = discord.Embed(title='Ybot helper', description='=택배 목록: 조회 가능한 택배 회사들을 불러옵니다.\n=택배 [운송장번호]: 자동적으로 회사를 확인해서, 해당 배송상태를 표시합니다. \n=택배 [운송장번호] [택배회사]: 해당 회사의 운송장번호를 조회하여, 배송상태를 표시합니다.', color=0x00aaaa)
                await message.channel.send(embed=embed)
                return
            else:
                if list_message[1] == "목록":
                    html = requests.get("http://info.sweettracker.co.kr/api/v1/companylist?t_key=cM2AMbcW6heHckZ4TeD84w").text
                    answer = ''
                    list_company = html.split('Code') #"Code":"
                    for i in range(len(list_company)-1):
                        answer = answer + ',' + html.split('"Name":"')[i+1].split('"')[0]
                    embed = discord.Embed(title='조회가능한 택배사 목록', description=answer.replace(',','',1), color=0x00aaaa)
                    await message.channel.send(embed=embed)
                else:
                    try:
                        test_data = list_message[2]
                    except:
                        try:
                            html = requests.get("https://info.sweettracker.co.kr/api/v1/recommend?t_key=cM2AMbcW6heHckZ4TeD84w&t_invoice=" + list_message[1]).text
                            company = html.split('"Code":"')[1].split('"')[0]
                        except:
                            embed = discord.Embed(title='에러', description='택배사 조회에 실패하였습니다. 택배회사를 기재해주시기 바랍니다.', color=0x00aaaa)
                            await message.channel.send(embed=embed)
                            return
                    else:
                        company = "111"
                        html = requests.get("http://info.sweettracker.co.kr/api/v1/companylist?t_key=cM2AMbcW6heHckZ4TeD84w").text
                        list_company = html.split('Code')
                        for i in range(len(list_company)-1):
                            if list_message[2] ==html.split('"Name":"')[i+1].split('"')[0] :
                                company = html.split('"Code":"')[i+1].split('"')[0]
                        if company == "111":
                            embed = discord.Embed(title='에러', description='존재하지 않는 택배사입니다. 다시한번 확인해주시기 바랍니다. ( "=택배 목록" )', color=0x00aaaa)
                            await message.channel.send(embed=embed)
                            return
                    data = 't_key=cM2AMbcW6heHckZ4TeD84w&t_code=' + company + '&t_invoice=' + list_message[1]
                    html = requests.get("https://info.sweettracker.co.kr/api/v1/trackingInfo?" + data).text
                    try:
                        test_data = html.split('"senderName":"')[1].split('"')[0]
                    except:
                        answer = html.split('"msg":"')[1].split('"')[0]
                        if answer == "유효하지 않은 운송장번호 이거나 택배사 코드 입니다.":
                            answer = '택배사 조회에 실패하였습니다. 택배회사를 기재해주시기 바랍니다.'
                        embed = discord.Embed(title='에러', description=answer, color=0x00aaaa)
                        await message.channel.send(embed=embed)
                    else:
                        result = html.split('"result":"')[1].split('"')[0]
                        if result == 'N':
                            embed = discord.Embed(title='에러', description='송장번호가 올바르지 틀리거나, 택배회사 전산 오류입니다.\n 택배회사를 기재해주시기 바랍니다. 기재후에도 지속적으로 오류가 발생할 경우 해당 택배사에게 문의해주시기 바랍니다.', color=0x00aaaa)
                            await message.channel.send(embed=embed)
                            return
                        sender_name = html.split('"senderName":"')[1].split('"')[0]
                        receiver_name = html.split('"receiverName":"')[1].split('"')[0]
                        item_name = html.split('"itemName":"')[1].split('"')[0]
                        if item_name == "":
                            item_name = "택배"
                        last_list = html.split('kind')
                        last_number = len(last_list) -2
                        where = html.split('"where":"')[last_number].split('"')[0]
                        kind_item =  html.split('"kind":"')[last_number].split('"')[0]
                        telephone = html.split('"telno":"')[last_number].split('"')[0]
                        time_item = html.split('"timeString":"')[last_number].split('"')[0]
                        #answer = "보낸 사람: " + sender_name + "\n받는 사람: " + receiver_name + "\n\n현재 상황: " + kind_item + "\n위치: " + where + "\n전화번호: " + telephone + "\n날짜 시간: " + time_item 
                        #embed = discord.Embed(title=item_name + '의 배송현황', description=answer, color=0x00aaaa)
                        embed = discord.Embed(title=item_name + '의 배송현황', color=0x00aaaa)
                        embed.add_field(name="보낸 사람: ", value=sender_name, inline=True)
                        embed.add_field(name="받는 사람: ", value=receiver_name, inline=True)
                        embed.add_field(name="현재 상황: ", value=kind_item, inline=True)
                        embed.add_field(name="위치: ", value=where, inline=True)
                        if telephone != "":
                            embed.add_field(name="전화번호: ", value=telephone, inline=True)
                        embed.set_footer(text="최근 업데이트: " + time_item)
                        await message.channel.send(embed=embed)
        except:
            embed = discord.Embed(title='에러', description='송장번호가 올바르지 않습니다.', color=0x00aaaa)
            await message.channel.send(embed=embed)
        return
    if message.content.startswith('=재난문자'):
        log_info(message.channel,message.author,message.content)
        try:
            try:
                data_false = list_message[1]
            except: #목록갯수
                list_search = 10
            else:
                list_search = int(list_message[1])
            try:
                data_false = list_message[2]
            except: #지역설정
                locate_search = '전국'
            else:
                locate_search = list_message[2]
            data = "https://m.search.naver.com/search.naver?query=" + locate_search + " 재난문자"
            html = requests.get(data).text
            max_search = len(html.split('<em class="area_name">'))-1
            if max_search < list_search:
                list_search = max_search
            embed = discord.Embed(title=locate_search + ' 재난문자 발령 현황', color=0x00aaaa)
            for i in range(list_search):
                city_name = html.split('<em class="area_name">')[i+1].split('</em>')[0]
                date_time = html.split('<time datetime="">')[i+1].split('</time>')[0]
                text = html.split('<span class="dsc _text">')[i+1].split('</span>')[0]
                embed.add_field(name=city_name, value='[' + date_time + ']:' + text, inline=False)
            await message.channel.send(embed=embed)
        except:
            embed = discord.Embed(title='에러', description='알수없는 오류가 발생하였습니다.', color=0x00aaaa)
            await message.channel.send(embed=embed)
        return
    if message.content.startswith('=이스터에그'):
        log_info(message.channel,message.author,message.content)
        message.channel.send("어머나! 이스터에그를 찾으셧네요!")
        return
    if message.content.startswith('=청소'):
        log_info(message.channel,message.author,message.content)
        try:
            amount = list_message[1]
        except:
            embed = discord.Embed(title="Ybot helper",description="=청소 [갯수]로 사용하실수 있습니다.", color=0x00aaaa)
            await message.channel.send(embed=embed)
            return
        try:
            await message.channel.purge(limit = int(amount))
            embed = discord.Embed(title="청소!",description=str(message.author) + "에의해" + amount + '개가 청소되었습니다.', color=0x00aaaa)
            await message.channel.send(embed=embed)
        except:
            embed = discord.Embed(title="Ybot helper",description="올바른값을 입력하세요.", color=0x00aaaa)
            await message.channel.send(embed=embed)
        return
    if message.content.startswith('=스팀'):
        log_info(message.channel,message.author,message.content)
        try:
             nickname = list_message[1]
        except:
            embed = discord.Embed(title="Ybot helper",description="닉네임을 적어주세요! 만약에 닉네임이 없다면 유저코드를 적어주세요.\n =스팀 [유저코드 혹은 아이디] [유저코드활성여부(아닐경우 미기재)]\n유저코드를 기재 할경우에는 유저코드를 활성화하셔야합니다.", color=0x00aaaa)
            await message.channel.send(embed=embed)
            return
        try:
             cache_data = list_message[2]
        except:
            mode = "id"
        else:
            mode = "profiles"
        html = requests.get("https://steamcommunity.com/" + mode + "/" + nickname + "/").text
        try:
            username = html.split('"personaname":"')[1].split('"')[0]
            embed = discord.Embed(title=username , url="https://steamcommunity.com/" + mode + "/" + nickname + "?l=koreana", color=0x00aaaa)
            try:
                data=html.split("This profile is private.")[1]
            except:
                status = ""
                is_Online = html.split('<div class="profile_in_game_header">')[1].split('</div>')[0]
                if is_Online == "Currently Offline":
                    status = "오프라인"
                elif is_Online == "Currently In-Game":
                    status = "게임 중"
                    status = status + "(" + html.split('<div class="profile_in_game_name">')[1].split('</div>')[0] + ")"
                elif is_Online == "Currently Online":
                    status = "온라인"
                else:
                    status = is_Online
                icon_url = html.split('<img src="')[5].split('">')[0]
                embed.add_field(name="상태:", value=status, inline=True)
                embed.set_thumbnail(url=icon_url)
                try:
                    since = html.split('since')[1].split('"')[0]
                    embed.add_field(name="최초가입일:", value=since, inline=True)
                except:
                    dummy = 0
                #embed.set_image(url=icon_url)
                try:
                    level = html.split('<span class="friendPlayerLevelNum">')[1].split('</span>')[0]
                    embed.add_field(name="레벨:", value=level, inline=True)
                    local_data = ""
                    for i in range(3):
                        cache_html1 = html.split('<div class="game_name">')[i+1].split('</div>')[0]
                        game_name =  cache_html1.split('">')[1].split('</a>')[0]
                        game_time = html.split('<div class="game_info_details">')[i+1].split('on record')[0].replace("hrs","시간").replace('	','').replace(' ','')
                        least_game = html.split('last played on')[i+1].split('</div>')[0].replace('	','').replace(' ','')
                        #game_time=""
                        local_data = local_data + "**" + game_name + "**:" + game_time + "플레이( 마지막 게임한 날짜:" + least_game + ")\n"
                    embed.add_field(name="최근 플레이한 게임:", value=local_data, inline=False)
                except:
                    dummy = 0
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(title="에러!",description="이 계정은 비공개 계정입니다.", color=0x00aaaa)
                await message.channel.send(embed=embed)
        except:
            try:
                answer = html.split('<h3>')[1].split('</h3>')[0]
                if answer == "The specified profile could not be found.":
                    answer = "요청하신 계정을 찾을수 없습니다. 만약에 닉네임이 없다면 유저코드를 적어주세요.\n =스팀 [유저코드] [유저코드활성여부(아닐경우 미기재)]\n유저코드를 기재 할경우에는 유저코드를 활성화하셔야합니다."
                embed = discord.Embed(title="에러!",description=answer, color=0x00aaaa)
                await message.channel.send(embed=embed)
            except:
                embed = discord.Embed(title="에러!",description="알수없는 오류가 발생하였습니다.", color=0x00aaaa)
                await message.channel.send(embed=embed)
        return
    if message.content.startswith('=사용자문제'):
        log_info(message.channel,message.author,message.content)
        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/emojis/673754223468609549.gif?v=1")
        await message.channel.send(embed=embed)
        return
    if message.content.startswith('=PUBG'):
        try:
            log_info(message.channel,message.author,message.content)
            try:
                nickname = list_message[1]
            except: #닉네임 설정
                embed = discord.Embed(title="에러!",description="닉네임을 기재하여 주세요.", color=0x00aaaa)
                await message.channel.send(embed=embed)
                return
            try:
                season = "/pc-2018-" + list_message[2]
            except: #시즌 설정
                season = ''
            embed = discord.Embed(title=nickname, color=0x00aaaa)
            html = requests.get("https://dak.gg/profile/" + nickname + season).text
            LastUpdate = html.split('<span>')[8].split('</span>')[0]
            embed.set_footer(text="최근 업데이트: " + LastUpdate)
            icon_url = html.split('<div class="userInfo">')[1].split('<img src="')[1].split('"')[0] #파싱 필요
            games = html.split('<div class="pa_sc pa_sc_big profile-')[1].split('"')[0]
            if games == "kakao":
                icon_url = "https://dak.gg" + icon_url
            embed.set_thumbnail(url=icon_url)
            data = ['솔로','솔로 1인칭','듀오','듀오 1인칭','스쿼드','스쿼드 1인칭']
            data4 = ['솔로','솔로 1인칭','듀오','듀오 1인칭','스쿼드','스쿼드 1인칭']
            for i in range(6):
                try:
                    cache = html.split('<div class="overview">')[i+1].split('<span class="top" style="visibility: hidden;">')[0]
                    data1 = cache.split('alt="')[1].split('"')[0]
                    data2 = cache.split('<span class="value">')[1].split('</span>')[0]
                    data3 = cache.split('<p class="win-stats">')[1].split('</p>')[0].replace('W','승').replace('T','탑').replace('L','패').replace("\n","").replace("\t","")
                    data4 = cache.split('<p class="value">')[1].split('</p>')[0].replace('\n','').replace('	','').replace(' ','')
                    data5 = cache.split('<p class="value">')[5].split('</p>')[0].replace('\n','').replace('	','').replace(' ','')
                    answer = "**" + data2 + "(" +data1 + ")**\n" + data3 + "\nK/D:" + data4 + "\n게임 수:" + data5
                    embed.add_field(name=data[i], value=answer, inline=True)
                except:
                    embed.add_field(name=data[i], value="기록 없음", inline=True)
            await message.channel.send(embed=embed)
        except:
            embed = discord.Embed(title="에러!", description="알수없는 오류가 발생하였습니다.\n[대표적인 발생원인]: 잘못된 닉네임 기재.", color=0x00aaaa)
            await message.channel.send(embed=embed)
        return
    if message.content.startswith('=레인보우식스'):
        log_info(message.channel,message.author,message.content)
        try:
                nickname = list_message[1]
        except: #닉네임 설정
            embed = discord.Embed(title="에러!",description="닉네임을 기재하여 주세요.", color=0x00aaaa)
            await message.channel.send(embed=embed)
            return
        html = requests.get('https://www.r6stats.com/stats/uplay/' + nickname).text
        try:
            embed = discord.Embed(title=nickname, color=0x00aaaa)
            icon_url = html.split('name="og:image" content="')[1].split('">')[0]
            embed.set_thumbnail(url=icon_url)
            level = html.split('<span class="quick-info__value">')[1].split('</span>')[0]
            play_time = html.split('<span class="quick-info__value">')[2].split('</span>')[0]
            match_count = html.split('<span class="stat-count">')[20].split('</span>')[0]
            KD = html.split('<span class="stat-count">')[24].split('</span>')[0]
            kill = html.split('<span class="stat-count">')[22].split('</span>')[0]
            death = html.split('<span class="stat-count">')[23].split('</span>')[0]
            win = html.split('<span class="stat-count">')[25].split('</span>')[0]
            lose = html.split('<span class="stat-count">')[26].split('</span>')[0]
            champion = html.split('alt="')[4].split('"')[0]
            headshot = html.split('<span class="stat-count">')[40].split('</span>')[0]
            headshot_persent = html.split('<span class="stat-count">')[41].split('</span>')[0]
            asia = html.split('<img src="https://cdn.r6stats.com/seasons/ranks/')[2].split('.svg"')[0]
            america = html.split('<img src="https://cdn.r6stats.com/seasons/ranks/')[1].split('.svg"')[0]
            europe = html.split('<img src="https://cdn.r6stats.com/seasons/ranks/')[3].split('.svg"')[0]
            rank = "■ 아시아: " + asia + "\n■ 미국: " + america + "\n■  유럽: " + europe
            embed.add_field(name="랭크:", value=rank, inline=True)
            embed.add_field(name="승/패:", value=win + "승/" + lose + "패", inline=True)
            embed.add_field(name="플레이시간:", value=play_time, inline=True)
            embed.add_field(name="킬:", value=kill, inline=True)
            embed.add_field(name="죽음: :", value=death, inline=True)
            embed.add_field(name="K/D:", value=KD, inline=True)
            embed.add_field(name="헤드샷:", value=headshot + "(" + headshot_persent + ")", inline=True)
            embed.add_field(name="레벨:", value=level, inline=True)
            embed.add_field(name="자주사용하는 챔피언:", value=champion, inline=True)
            await message.channel.send(embed=embed)
            return
        except: #닉네임 설정
            try:
                error_log = html.split('<p class="result-count">')[1].split('</p>')[0]
                if error_log == "No results returned":
                    error_log = "닉네임을 찾을수가 없습니다"
                embed = discord.Embed(title="에러!",description=error_log, color=0x00aaaa)
                await message.channel.send(embed=embed)
                return
            except:
                embed = discord.Embed(title="에러!",description="알수없는 에러가 발생하였습니다..", color=0x00aaaa)
                await message.channel.send(embed=embed)
                return
    if message.content.startswith('=오버워치'):
        log_info(message.channel,message.author,message.content)
        try:
                nickname = list_message[1]
        except: #닉네임 설정
            embed = discord.Embed(title="에러!",description="닉네임을 기재하여 주세요.", color=0x00aaaa)
            await message.channel.send(embed=embed)
            return
        nickname = nickname.replace("#","%23").replace(" ","%20")
        try:
                mode = list_message[2]
        except:
            embed = discord.Embed(title="Ybot helper", description='=오버워치 [닉네임] [(빠른대전/경쟁전)] 둘중하나를 무조건 선택해주셔야 합니다.', color=0x00aaaa)
            await message.channel.send(embed=embed)
            return
        else:
            html = requests.get('https://overwatch.op.gg/search/?playerName=' + nickname).text
            usercode = html.split('data-uid="')[1].split('"')[0]
            #usercode = "111029242162120119198225"
            try:
                embed = discord.Embed(title=nickname, color=0x00aaaa)
                if mode == "빠른대전":
                    html1 = requests.get('https://overwatch.op.gg/detail/quick/' + usercode).text
                    icon_url = html1.split('<img src="')[9].split('"')[0]
                    LastUpdate = html1.split('<b>')[1].split('</b>')[0]
                    embed.set_thumbnail(url=icon_url)
                    embed.set_footer(text="최근 업데이트: " + LastUpdate)
                    KD = html1.split('<span>')[5].split('</span>')[0]
                    play_time = html1.split('<span>')[6].split('</span>')[0].replace('hours','시간').replace('hour','시간').replace('mins','분').replace('min','분')
                    win = html1.split('<span>')[7].split('</span>')[0].replace('\n','').replace('	','').replace(' ','').replace('W','승')
                    fire = html1.split('<span>')[10].split('</span>')[0].replace("<em>","").replace("</em>","").replace('hours','시간').replace('hour','시간').replace('mins','분').replace('min','분')
                    heros_cache = html1.split('<div class="Image">')[1]
                    heros = heros_cache.split('</div>')[1].split('</td>')[0].replace('\n','').replace('	','').replace(' ','')
                    heros_time = heros_cache.split('<td class="ContentCell">')[2].split('</td>')[0].replace('hours','시간').replace('hour','시간').replace('mins','분').replace('min','분')
                    embed.add_field(name="플레이시간:", value=play_time, inline=True)
                    embed.add_field(name="K/D:", value=KD, inline=True)
                    embed.add_field(name="승리:", value=win, inline=True)
                    embed.add_field(name="전체 폭주량:", value=fire, inline=True)
                    embed.add_field(name="주 캐릭터:", value=heros + "(" + heros_time + ")", inline=True)
                    await message.channel.send(embed=embed)
                elif mode == "경쟁전":
                    html1 = requests.get('https://overwatch.op.gg/detail/overview/' + usercode).text
                    data1 = ['■ 돌격: ','■ 공격: ','■ 지원: ']
                    icon_url = html1.split('<img src="')[9].split('"')[0]
                    LastUpdate = html1.split('<b>')[1].split('</b>')[0]
                    embed.set_thumbnail(url=icon_url)
                    embed.set_footer(text="최근 업데이트: " + LastUpdate)
                    answer1 = ""
                    answer2 = ""
                    answer3 = ""
                    for i in range(3):
                        cache_data = html1.split('<div class="role-tier__content">')[i+1]
                        try:
                            point = cache_data.split('<b class="role-tier__score text-navy">')[1].split('</b>')[0]
                            rank2 = cache_data.split('<span class="role-tier__text text-navy">')[1].split('</span>')[0].replace('\n','').replace('	','').replace(' ','')
                            rank2 = rank2.replace("Bronze","브론즈").replace("Sliver","실버").replace("Gold","골드").replace("Platinum","플레티넘").replace("Diamond","다이야몬드").replace("Master","마스터").replace("Grandmaster","그랜드 마스터")
                            answer1 = answer1 + data1[i] + point + "(" + rank2 + ')\n'
                        except:
                            answer1 = answer1 + data1[i] + "(배치 전)\n"
                    embed.add_field(name="랭크:", value=answer1, inline=True)
                    for i in range(3):
                        cache_data = html1.split('<span class="role-tier__winlose">')[i+1].split('</span>')[0].replace('\n','').replace('	','').replace(' ','')
                        cache_data = cache_data.replace("W","승 ").replace("D","무 ").replace("L","패").replace("/"," ")
                        answer2 = answer2 + data1[i] + cache_data + '\n'
                    embed.add_field(name="승/무/패:", value=answer2, inline=True)
                    count = 2
                    for i in range(3):
                        cache_data = html1.split('<td class="ContentCell">')[count].split('</td>')[0].replace('\n','').replace('	','').replace(' ','')
                        cache_data = cache_data.replace('hours','시간').replace('hour','시간').replace('mins','분').replace('min','분')
                        answer3 = answer3 + data1[i] + cache_data + '\n'
                        count = count + 4
                    KD = html1.split('<span>')[12].split('</span>')[0]
                    kill = html1.split('<span>')[13].split('</span>')[0]
                    death = html1.split('<span>')[14].split('</span>')[0]
                    deal = html1.split('<span>')[15].split('</span>')[0]
                    heal = html1.split('<span>')[16].split('</span>')[0]
                    fire = html1.split('<span>')[19].split('</span>')[0].replace("<em>","").replace("</em>","").replace('hours','시간').replace('hour','시간').replace('mins','분').replace('min','분')
                    heros_cache = html1.split('<div class="Image">')[1]
                    heros = heros_cache.split('</div>')[1].split('</td>')[0].replace('\n','').replace('	','').replace(' ','')
                    heros_time = heros_cache.split('<td class="ContentCell">')[2].split('</td>')[0].replace('hours','시간').replace('hour','시간').replace('mins','분').replace('min','분')
                    embed.add_field(name="플레이시간:", value=answer3, inline=True)
                    embed.add_field(name="K/D:", value=KD, inline=True)
                    embed.add_field(name="평균 킬:", value=kill, inline=True)
                    embed.add_field(name="평균 죽음:", value=death, inline=True)
                    embed.add_field(name="평균 딜량:", value=deal, inline=True)
                    embed.add_field(name="평균 힐량:", value=heal, inline=True)
                    embed.add_field(name="전체 폭주량:", value=fire, inline=True)
                    embed.add_field(name="주 캐릭터:", value=heros + "(" + heros_time + ")", inline=True)
                    await message.channel.send(embed=embed)
                else:
                    embed = discord.Embed(title="Ybot helper", description='=오버워치 [닉네임] [(빠른대전/경쟁전)] 둘중하나를 무조건 선택해주셔야 합니다.', color=0x00aaaa)
                    await message.channel.send(embed=embed)
                return
            except:
                embed = discord.Embed(title="에러!",description="검색에 실패하였습니다. 배틀태그까지 적는것을 권장합니다.", color=0x00aaaa)
                await message.channel.send(embed=embed)
    if message.content.startswith('=따라하기'):
        log_info(message.channel,message.author,message.content)
        embed = discord.Embed(title="따라하기",description=message.content.replace("=따라하기 ","") , color=0x00aaaa)
        embed.set_footer(text="요청자: " + str(message.author))
        await message.channel.send(embed=embed)

client.run('NjgwNjk0NzYzMDM2NzM3NTM2.XlDobg.PqT_o5NMmA4atyRZl1WKVdGISD8')
