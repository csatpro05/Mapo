import discord
import time
import random
from discord.ext import commands
bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready() : 
    print('Konnichiwa! Futaro kun!')
    day = time.localtime().tm_wday

@bot.command(aliases = ['유'])
async def sex(ctx) :
    await ctx.reply('종')

@bot.command(aliases = ['random'])
async def random_(ctx, *ran) :
    result = random.chioce(ran)
    await ctx.reply(result)


@bot.command(aliases = ['시간표', 'timetable', ])
async def timetable_(ctx) :
    day = time.localtime().tm_wday
    dic = {'k1':'국어A', 'k2':'국어B', 'e1':'영어A', 'e2':'영어B', 'm1':'수학', 'h1':'한국사', 's1':'통사', 'sc1':'과학1', 'sc2':'과학2', 'sc3':'과학3', 'sc4':'과학4', 'c1':'정보', 'a1':'미술', 'cr1':'창진', 'ex1':'과실', 'cr2':'창특', 'mu1':'음악', 'pe1':'체육', 'cr3':'창체'}
    if day == 0 :
        t1, t2, t3, t4, t5, t6, t7 = dic['h1'], dic['e2'], dic['sc3'], dic['m1'], dic['k1'], dic['k2'], dic['c1']
    elif day == 1 :
        t1, t2, t3, t4, t5, t6, t7 = dic['sc2'], dic['k1'], dic['s1'], dic['m1'], dic['c1'], dic['e1'], dic['h1']
    elif day == 2 :
        t1, t2, t3, t4, t5, t6, t7 = dic['sc1'], dic['m1'], dic['a1'], dic['h1'], dic['e1'], dic['cr1'], dic['c1']
    elif day == 3 :
        t1, t2, t3, t4, t5, t6, t7 = dic['sc4'], dic['e1'], dic['m1'], dic['ex1'], dic['s1'], dic['s1'], dic['cr2']
    elif day == 4 :
        t1, t2, t3, t4, t5, t6, t7 = dic['k1'], dic['pe1'], dic['mu1'], dic['s1'], dic['cr3'], dic['cr3'], '---'
            
    await ctx.send(f'```\n{t1}    8:20 ~ 9:05\n{t2}    9:15 ~ 10:00\n{t3}    10:10 ~ 10:55\n{t4}    11:05 ~ 11:50\n점심시간\n{t5}    01:00 ~ 01:45\n{t6}    01:55 ~ 02:40\n{t7}    02:50 ~ 03:35\n```')

@bot.command(aliases = ['fac'])
async def factorization_(ctx, *, var) : 
    cbn = var.replace(" ", "")          # List로 변환
    cbn = list(cbn)
    x1 = cbn.index('x') - 1             # x^2 계수가 1이라면 1 삽입
    if x1 == -1 :
        cbn.insert(0, '1')
        x1 += 1
    cbn = cbn[:x1+1] + cbn[x1+3:]       
    cbn.insert(x1+1, 'x1')
    try :                               # x의 계수가 0이라면 0 삽입
        x2 = cbn.index('x')
    except :
        cbn.insert(x1 + 2, '+')
        cbn.insert(x1 + 3, '0')
        cbn.insert(x1 + 4, 'x')
        x2 = cbn.index('x')
    x2 -= 1
    dig2 = cbn[x2]                      # x의 계수가 1이라면 1 삽입
    if dig2.isdigit() == False :
        cbn.insert(x2+1, '1')
        x2 += 1
    cbn = cbn[:x2+1] + cbn[x2+2:]
    cbn.insert(x2+1, 'x2')    
    dig3 = cbn[-1]                      # 상수가 0이라면 0 삽입
    if dig3.isdigit() == False :        
        cbn.append('+')
        cbn.append('0')
    pm = cbn[0]                         # x^2의 부호가 +라면 + 삽입
    if pm.isdigit() == True :
        cbn.insert(0, '+')
    tw1 = cbn.index('x1')               # 계수 중 두자릿수가 존재한다면 List에 따로 존재하는 수를 합체
    i = 1
    one = 1
    new1, new2, new3 = 0, 0, 0
    if tw1 >= 3 :
        while cbn[tw1 - i] not in ['+', '-'] :
            pop = cbn.pop(tw1 - i)
            pop = int(pop) * one
            new1 += pop
            one *= 10
            i += 1
        cbn.insert(1, str(new1))
        one = 1
        i = 1    
    tw2 = cbn.index('x2')
    if tw2 >= 6 :
        while cbn[tw2 - i] not in ['+', '-'] :
            pop = cbn.pop(tw2 - i)
            pop = int(pop) * one
            new2 += pop
            one *= 10
            i += 1
        cbn.insert(4, str(new2))
        one = 1
        i = 1
    if len(cbn) >= 9 :
        while cbn[-1] not in ['+', '-'] :
            pop = cbn.pop(-1)
            pop = int(pop) * one
            new3 += pop
            one *= 10
        cbn.insert(8, str(new3))
    a, b, c = int(cbn[cbn.index('x1')-1]), int(cbn[cbn.index('x2')-1]), int(cbn[-1])    # x^2의 계수, 상수항 각각의 약수 구하기
    pm1, pm2, pm3 = cbn[cbn.index('x1')-2], cbn[cbn.index('x2')-2], cbn[-2]
    a1div = []
    c1div = []
    for a1 in range(1, a+1):
        if a%a1 == 0 and pm1 == '+' :
            a1div.append([a1, a//a1])
        if a%a1 == 0 and pm1 == '-' : 
            a1div.append([a1, -(a//a1)])
            a1div.append([-a1, a//a1])
        else:
            a1 = None
    if c != 0 :
        for c1 in range (1, c+1) :
            if c%c1 == 0 and pm3 == '+' :
                c1div.append([c1, c//c1])
                c1div.append([-c1, -(c//c1)])        
            if c%c1 == 0 and pm3 == '-' :
                c1div.append([c1, -(c//c1)])
                c1div.append([-c1, c//c1])
            else:
                c1 = None
    elif c == 0 :
        c1div.append([0, 0])
    if cbn[3] == '+' :                  # x의 계수와 부호 합치기
        del cbn[3]
    elif cbn[3] == '-' :
        del cbn[3]
        cbn[3] = str(-int(cbn[3]))
    pflist = []                         # x 계수 계산
    for x1pf in a1div : 
        x1pf1, x1pf2 = x1pf[0], x1pf[1]
        for x2pf in c1div :
            x2pf1, x2pf2 = x2pf[0], x2pf[1]
            if x1pf1 * x2pf2 + x1pf2 * x2pf1 == int(cbn[3]) :
                pflist.append([x1pf1, x2pf1, x1pf2, x2pf2])
            else : 
                pass
    if c1div == [[0, 0]] :
        pflist.append([a1div[0][0], 0, a1div[0][1], int(cbn[3])])
    pflistlen = len(pflist)             # list 중복 정리
    if len(pflist) % 2 == 0 :
        pflist = pflist[:len(pflist) // 2]
    try :
        pflist = pflist[0]
        pflistfinal = []                    # 결과식 제작
        for pfliststr in pflist :
            pflistfinal.append(str(pfliststr))
        
        if int(pflistfinal[1]) >= 0 :       # 부호 붙이기
            pflistfinal[1] = '+' + pflistfinal[1]
        if int(pflistfinal[3]) >= 0 :
            pflistfinal[3] = '+' + pflistfinal[3]
        final = f'({pflistfinal[0]}x{pflistfinal[1]})({pflistfinal[2]}x{pflistfinal[3]})'
        finallist = list(final)
        '''for finalone in finallist :      # 1 지우기
            if finallist.count('1') >= 1 :
                finalindex = finallist.index('1')
                del finallist[finalindex]
            else :
                pass'''

        final = ''.join(finallist)          # List를 문자열로 전환
        print(final)
        alpha = -(pflist[1] / pflist[0])    # 해 구하기
        beta = -(pflist[3] / pflist[2])
        if alpha == beta :                  # 중근 
            beta = None
        print(alpha, beta)
        
        if beta != None :                   # Discord에 메세지 보내기
            await ctx.send(f'{final}   해 : x={alpha}, x= {beta}')
        elif beta == None :
            await ctx.send(f'{final}   해 : x={alpha} (중근)')
    except :
        await ctx.send('되겠냐')



    


    
    



@bot.command(aliases = ['mute'])
async def mute_(ctx, user:discord.User) :
    await user.edit(mute = True)

@bot.command(aliases = ['unmute'])
async def unmute_(ctx, user:discord.User) :
    await user.edit(mute = False)

@bot.command(aliases = ['deafen'])
async def deafen_(ctx, user:discord.User) :
    await user.edit(deafen = True)

@bot.command(aliases = ['undeafen'])
async def undeafen_(ctx, user:discord.User) :
    await user.edit(deafen = False)





    
        
        
        
        
                



    

    







bot.run('OTA5NjUxMjQ5MzQ1OTk4ODc4.YZHYvg.LbxNGclahJckwecXNiqS-sDLusI')
