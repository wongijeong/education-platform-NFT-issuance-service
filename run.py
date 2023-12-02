from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify

app = Flask(__name__)
app.secret_key = "lkjds#2-1j@dsp!ldaskfj"

URL = "test"
ID = "student"
PW = "123"
ID_T = "teacher"
PW_T = "321"

#메인 로그인#
@app.route('/')
@app.route('/login')
def login():
    return render_template("login.html")
    
#학생 페이지들#
@app.route("/start", methods = ['POST', 'GET'])
def start():
    if request.method == 'POST':
        global ID, PW
        _id_ = request.form['loginId']
        _password_ = request.form['loginPw']
        if ID == _id_ and PW == _password_:
            session["userID"] = _id_
            return render_template("s_main.html")
        else:
            flash("아이디 또는 비밀번호가 잘못되었습니다.")
            return redirect(url_for('login'))

@app.route("/start_t", methods = ['POST', 'GET'])
def start_t():
    if request.method == 'POST':
        global ID, PW
        _id_ = request.form['loginId']
        _password_ = request.form['loginPw']
        if ID_T == _id_ and PW_T == _password_:
            session["userID"] = _id_
            return render_template("Problem_management.html")
        else:
            flash("아이디 또는 비밀번호가 잘못되었습니다.")
            return redirect(url_for('login'))

@app.route('/s_main')
def s_main():
    return render_template("s_main.html")
    
#@app.route('/nft_check_kor')  // OpeaSea 보기로 바꿈
#def nft_check_kor():
#    return render_template("nft_check_kor.html")
    
@app.route('/nft_check_math')
def nft_check_math():
    return render_template("nft_check_math.html")

@app.route('/nft_check_eng')
def nft_check_eng():
    return render_template("nft_check_eng.html")

@app.route('/nft_check_crea')
def nft_check_crea():
    return render_template("nft_check_crea.html")

@app.route('/nft_check_gen')
def nft_check_gen():
    return render_template("nft_check_gen.html")

@app.route('/nft_check_memory')
def nft_check_memory():
    return render_template("nft_check_memory.html")

@app.route('/problem_kor_main')
def problem_kor_main():
    return render_template("problem_kor_main.html")

@app.route('/problem_math_main')
def problem_math_main():
    return render_template("problem_math_main.html")

@app.route('/problem_eng_main')
def problem_eng_main():
    return render_template("problem_eng_main.html")

@app.route('/problem_crea_main')
def problem_crea_main():
    return render_template("problem_crea_main.html")

@app.route('/problem_gen_main')
def problem_gen_main():
    return render_template("problem_gen_main.html")

@app.route('/problem_kor')
def problem_kor():
    return render_template("problem_kor.html")

@app.route('/problem_math')
def problem_math():
    return render_template("problem_math.html")

@app.route('/problem_eng')
def problem_eng():
    return render_template("problem_eng.html")

@app.route('/problem_crea')
def problem_crea():
    return render_template("problem_crea.html")

@app.route('/problem_gen')
def problem_gen():
    return render_template("problem_gen.html")

@app.route('/upload')
def upload():
    return render_template("upload.html")

#여기부터 교사 페이지#

@app.route('/Problem_management')
def probmle_management():
    return render_template("problem_management.html")

@app.route('/problem_upload')
def problem_upload():
    return render_template("problem_upload.html")

@app.route('/group_management')
def group_management():
    return render_template("group_management.html")

@app.route('/group_management_2')
def group_management_2():
    return render_template("group_management_2.html")

@app.route('/group_management_3')
def group_management_3():
    return render_template("group_management_3.html")

@app.route('/group_management_4')
def group_management_4():
    return render_template("group_management_4.html")

@app.route('/group_management_5')
def group_management_5():
    return render_template("group_management_5.html")

@app.route('/group_management_6')
def group_management_6():
    return render_template("group_management_6.html")

@app.route('/group_management_vote')
def group_management_vote():
    return render_template("group_management_vote.html")

@app.route('/group_management_vote_closing')
def group_management_vote_closing():
    return render_template("group_management_vote_closing.html")

@app.route('/nft_publication')
def nft_publication():
    return render_template("nft_publication.html")

@app.route('/getFromHtml', methods=['POST', 'GET']) #호출하는 부분. 직전에다가 URL 값만 가져오면됨.
def MyPythonCode():
    #해당 함수 변수 사항
    # browser = webdriver.Chrome("D:\gicap\Work_Code\chromedriver.exe") 의 드라이버 링크 잡기
    # path경로 설정
    #CID.txt 파일 경로 설정(flask 내부)

    if request.method == 'POST':
        global URL
        URL = request.form['numm']
    print("@@@@"+URL+"@@@@")
    
    from tkinter import messagebox
    from tkinter import Tk
    from select import select
    from webbrowser import get
    from selenium import webdriver
    from bs4 import BeautifulSoup
    from collections import OrderedDict
    import json
    import time
    import urllib.request #URL에서 이미지 다운로드
    import sys #argv 쓰기 위해
    import os #파일 있나 확인하기 위해
    
    root = Tk()
    root.geometry("0x0-0+0")
    messagebox.showinfo(title="IPFS 업로드", message="확인 버튼을 누르면 이미지 업로드가 진행됩니다.")
    name_indexfile = "test_index.txt"
    webpw ="Genius6514"
    webid ="geniusedu313@gmail.com"

    def Imageindexing(path, Filename, Fileexten, buf_count): #다운받은 이미지에 대해 인덱스파일에 기록
    
        # "순번    파일명.확장자" 양식으로 인덱스 저장 (추후 JSON속성들을 끌어다가 추가하면 될듯)
        with open(path + name_indexfile,"a") as file: #수정모드로 맨 뒤에 기록
            file.write(str(buf_count)+"\t"+Filename+Fileexten+"\n")


    #def ImageDownload(): #테스트용 함수
        #url = "https://dorm.kyonggi.ac.kr:446/images/Khostel/templates/B0001/images/sub/sub02_01_img.jpg" #입력URL 가정
    def ImageDownload(url):
        path = "D:/gicap/data/"  # 작업 경로
        Fileexten = ".jpg" #확장자 지정

        #다운로드 전에 기존 인덱스 파일이 있는지 확인하고 없다면 생성(O)
        if not os.path.isfile(path+name_indexfile): # 인덱스 텍스트파일 없으면 생성
            print("기존 인덱스 파일이 감지되지 않아 생성함") #확인용
            with open(path+name_indexfile,"w") as file: #파일 생성
                file.write('0\n') #이미지 파일 순번 초기셋팅

        #인덱스 파일에서 맨 윗줄에 있는 순번을 읽어옴(O)
        with open(path+name_indexfile,"r") as file:
            buf_count = file.readline().strip() 

        #buf_count는 (증가된)현재 사용할 수 있는 번호
        buf_count = int(buf_count) + 1 #인덱스 값 증가(O)

        Filename = str(buf_count) # 파일 이름 뒤에 순번붙이기(O)         예시) 1.jpg


        #인덱스 파일에서 맨 윗줄에 있는 순번을 하나 증가하여 기록(방식: 전체백업 - w로 인덱스숫자 작성 - a로 [1:]에 대해 아랫부분 정보 추가)
        with open(path+name_indexfile,"r") as file: # 전체 텍스트 임시저장
            lines = file.readlines()

        with open(path+name_indexfile,"w") as file: # 인덱스 번호만 다시 작성(아랫부분은 다 지워짐)
            file.write(str(buf_count)+"\n") 
        
        with open(path+name_indexfile,"a") as file: #없어졌던 아랫부분 정보들 쓰기 
            file.writelines(lines[1:]) # 0번줄 빼고 모든 라인 작성
        
        path_full = path+Filename+Fileexten # 풀네임 D:/gicap/Test1.jpg 형식

        urllib.request.urlretrieve(url, path_full) #이미지 다운, path_full은 저장할 파일 이름
        Imageindexing(path, Filename, Fileexten, buf_count) #(이미지다운 이후) 인덱스 파일에 내용 추가작업


        # 옵션 생성
        #options = webdriver.ChromeOptions()
        # 창 숨기는 옵션 추가
        #options.add_argument("headless")
        #browser = webdriver.Chrome("D:\gicap\Work_Code\chromedriver.exe",options=options)   

        browser = webdriver.Chrome("D:\gicap\Work_Code\chromedriver.exe")   #창 보이기
        urlp ="https://app.pinata.cloud/signin"
        browser.implicitly_wait(10) #페이지가 로딩될때 까지 최대 10초 기다림
        browser.get(urlp)

        #아이디 입력부분
        id = browser.find_element_by_css_selector("#root > div > div > div > div > div.overflow-hidden.card > div.pt-0.card-body > div.p-2 > form > div:nth-child(1) > div:nth-child(1) > input")
        id.click()
        id.send_keys(webid)

        #비밀번호 입력부분
        pw = browser.find_element_by_css_selector("#root > div > div > div > div > div.overflow-hidden.card > div.pt-0.card-body > div.p-2 > form > div:nth-child(1) > div:nth-child(2) > input")
        pw.click()
        pw.send_keys(webpw)

        #로그인 버튼
        login_btn = browser.find_element_by_css_selector("#root > div > div > div > div > div.overflow-hidden.card > div.pt-0.card-body > div.p-2 > form > div:nth-child(1) > button")
        login_btn.click()
        time.sleep(0.5)

        #이미지 업로드
        upload = browser.find_element_by_css_selector("#layout-wrapper > div.mt-4.container-fluid > div > div > div > div > div:nth-child(1) > div > div.align-self-center.col-sm-5.col-xl-3 > div > div > button")
        upload.click()       #upload버튼 클릭
        time.sleep(1)
        upload_file=browser.find_element_by_css_selector("#layout-wrapper > div.mt-4.container-fluid > div > div > div > div > div:nth-child(1) > div > div.align-self-center.col-sm-5.col-xl-3 > div > div > div > a:nth-child(2)")
        upload_file.click()  #file버튼 클릭
        time.sleep(0.5)
        time.sleep(4)
        Imagepath = path + Filename + Fileexten    #저장장소에서 이미지 가져오기
        select_file = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/input')
        select_file.send_keys(Imagepath)  #이미지 경로 대입
        time.sleep(1)
        imgname = Filename + Fileexten   #저장할 이미지 이름
        file_name = browser.find_element_by_xpath('//*[@id="thresholdconfig"]')
        file_name.clear()
        file_name.send_keys(imgname)
        time.sleep(0.5)
        upload_confirm = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/button')
        upload_confirm.click()   #upload 확인 버튼 누르기
        time.sleep(20) #피나타 속도를 감안하여 높게 잡음

        #이미지 CD 가져오기
        html = browser.page_source
        soup = BeautifulSoup(html)
        totallname = soup.select('td > a')
        totallcd = soup.select('.pinata-link-button.pinata-mono')

        time.sleep(2)
        j=0
        for cd in totallcd:    #이미지의 cd값 찾기      
            if totallname[j].text.strip() == imgname: 
                imgcd = cd.text.strip()         
            j=j+1
        time.sleep(2)

        #json 만들기
        #JSON 생성 이전 폴더를 생성      EX) 1\1.JSON   2\2.JSON 
        if not os.path.exists(path+Filename):
            os.makedirs(path+Filename)
        else :
            print("JSON생성을 위한 영역의 메시지. 생성하려는 순번의 폴더가 이미 존재함")
        file_data  = OrderedDict()
        file_data["name"] = imgname
        file_data["description"] = "unique Calculus problem solution"
        jsoncd = "ipfs://" + imgcd   
        file_data["image"] = jsoncd     # CID 를 가지고 index.html로 가져가야됨
        file_data["numer"] = str(buf_count) 
        jsonname = Filename +'.json'
        with open(path+Filename+'/'+jsonname, 'w', encoding="utf-8") as make_file:
            json.dump(file_data,make_file, ensure_ascii=False, indent="\t")
        time.sleep(5)

        #json 업로드
        upload.click()       #upload버튼 클릭
        time.sleep(1)
        upload_file=browser.find_element_by_css_selector("#layout-wrapper > div.mt-4.container-fluid > div > div > div > div > div:nth-child(1) > div > div.align-self-center.col-sm-5.col-xl-3 > div > div > div > a:nth-child(1)")
        upload_file.click()  #folder버튼 클릭
        time.sleep(0.5)
        Jsonpath = path + Filename  #파일 폴더에서 생성된 json파일 가져오기
        print(Jsonpath)
        select2_file = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/input')
        select2_file.send_keys(Jsonpath)  #json파일 경로 대입
        time.sleep(1)
        jsonfoldername = "test"+Filename   #저장할 파일 이름
        folder_name = browser.find_element_by_xpath('//*[@id="thresholdconfig"]')
        folder_name.clear()
        folder_name.send_keys(jsonfoldername)
        time.sleep(0.5)
        upload2_confirm = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/button')
        upload2_confirm.click()   #upload 확인 버튼 누르기
        time.sleep(30) #피나타 속도를 감안하여 높게 잡음
        messagebox.showinfo(title="IPFS 업로드 완료", message="이미지 업로드가 완료되었습니다. 확인 버튼을 눌러주세요.")

        
        #JSON CID 가져와서 텍스트파일에 메모 jsonfoldername
        html = browser.page_source
        soup = BeautifulSoup(html)
        totallname = soup.select('td > a')
        totallcd = soup.select('.pinata-link-button.pinata-mono')

        time.sleep(2)
        j=0
        for cd in totallcd:    #이미지의 cd값 찾기   

            if totallname[j].text.strip() == jsonfoldername:  
                PURE_JSONCID = cd.text.strip()  
                break
            j=j+1
        
        with open('D:/gicap/app/static/data/CID.txt',"w") as file:  #CID.txt 파일 경로
            file.write(PURE_JSONCID)
        #return render_template("nft_publication.html") #여기가 아닌가..
        

    ImageDownload(URL) # 파일 실행시 가져오는 URL의 이미지 다운로드
    return render_template("nft_publication.html")
    
    #ImageDownload() #테스트용 함수호출



    # 이하 메모
    # python .\ImageDownload.py "https://dorm.kyonggi.ac.kr:446/images/Khostel/templates/B0001/images/sub/sub02_01_img.jpg"y "https://dorm.kyonggi.ac.kr:446/images/Khostel/templates/B0001/images/sub/sub02_01_img.jpg"


if __name__ == '__main__':
    app.run(debug=True)