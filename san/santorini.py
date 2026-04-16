import streamlit as st
import time

st.set_page_config(page_title="가자! 산토리니!!", page_icon="🛫")
if 'step' not in st.session_state:
   st.session_state.step = 0

#시작, q1,q2,q3 총 4개
steps = 3

#진행바 첫화면 결과 뺴고 출력
if st.session_state.step != 0 and st.session_state.step not in ["A-1.a", "A-1.b", "A-2.a", "A-2.b", "B-1.a", "B-1.b", "B-2.a", "B-2.b"]:
   if st.session_state.step == 1 or st.session_state.step in ["A", "B"]:
      progress_bar = 1 / 3
   elif st.session_state.step in ["A-1", "A-2", "B-1", "B-2"]:
      progress_bar = 2 / 3
   st.progress(progress_bar)
   st.write(f'진행률: {int(progress_bar * 100)}%')

#0단계 시작
if st.session_state.step == 0:
   st.title("산토리니 여행 가이드 🗺️")
   st.write("나와 가장 잘 맞는 산토리니의 명소들을 알수있는 여행 산BTI!! 🧳")
   if st.button("산토리니 테스트 시작하기! 🔥"):
      st.session_state.step = 1
      st.rerun()


#1단계[:A,B]
elif st.session_state.step == 1:
   st.subheader('Q1.내가 추구하는 여행은?')
   cho1, cho2 = st.columns(2)

#1단계 중!!!
   with cho1:
      if st.button("눈이 즐거운 여행"):
         #달라짐
         st.session_state.step = "A"
         st.rerun

   with cho2:
      if st.button( "많은걸 경험하는 여행"):
        st.session_state.step = "B"
        st.rerun

#2당계로 넘어감 [A : A-1,A-2]
elif st.session_state.step == "A":
   st.subheader("Q2.어디가 더 좋을까?")
   cho1, cho2 = st.columns(2)

   with cho1:
      if st.button("한적하고 조용한 곳"):
         #달라짐
         st.session_state.step = "A-1"
         st.rerun

   with cho2:
      if st.button( "아름답기로 이미 유명한 곳"):
        st.session_state.step = "A-2"
        st.rerun

#3당계로 넘어감 [A-1]
elif st.session_state.step == "A-1":
   st.subheader("Q3.어떤 바람을 맞으며 자고싶어?")
   cho1, cho2 = st.columns(2)

   with cho1:
      if st.button("바닷바람"):
         #달라짐
         st.session_state.step = "A-1.a"
         st.rerun

   with cho2:
      if st.button( "산들바람"):
        st.session_state.step = "A-1.b"
        st.rerun

#3단계 [A-2]
elif st.session_state.step == "A-2":
   st.subheader("Q3.너가 추구하는 건?")
   cho1, cho2 = st.columns(2)

   with cho1:
      if st.button("사진찍기 최고의 장소!"):
         #달라짐
         st.session_state.step = "A-2.a"
         st.rerun

   with cho2:
      if st.button( "사진으론 못담는 경치"):
        st.session_state.step = "A-2.b"
        st.rerun

#2단계 [B]
elif st.session_state.step == "B":
   st.subheader("Q2.더 끌리는건?")
   cho1, cho2 = st.columns(2)

   with cho1:
      if st.button("이곳만의 특별함이 있는곳!"):
         #달라짐
         st.session_state.step = "B-1"
         st.rerun

   with cho2:
      if st.button( "활동적인 체험을 할 수 있는곳"):
        st.session_state.step = "B-2"
        st.rerun

#3단계 [b-1]
elif st.session_state.step == "B-1":
   st.subheader("Q3.어디가 더 끌려??")
   cho1, cho2 = st.columns(2)

   with cho1:
      if st.button("산토리니의 상징적인 곳"):
         #달라짐
         st.session_state.step = "B-1.a"
         st.rerun

   with cho2:
      if st.button( "산토리니의 숨은 보석"):
        st.session_state.step = "B-1.b"
        st.rerun

#3단계 [ㅠ-2]
elif st.session_state.step == "B-2":
   st.subheader("Q3.제대로 여행을 즐기기 위해선?")
   cho1, cho2 = st.columns(2)

   with cho1:
      if st.button("산토리니의 역사가 궁금해!"):
         #달라짐
         st.session_state.step = "B-2.a"
         st.rerun

   with cho2:
      if st.button( "투어지!!"):
        st.session_state.step = "B-2.b"
        st.rerun


#로딩 화면
elif "Result" in str(st.session_state.step):
   with st.spinner('당신에게 딱맞는 장소를 찾는중...'):
      time.sleep(1.5)

#꾸미깅 히히

   st.balloons()
   st.header('💕당신의 소울 명소 분석 완료!!!')

#결과

if st.session_state.step == "A-1.a":
   st.success("📍 **이오스** 🏝️")
   st.write("산토리니에서 가장 조용한 섬으로, 자연이 그대로 보존되어 있습니다. 이오스 섬은 산토리니의 다른 지역과 비교해 훨씬 더 한적하고 조용한 분위기를 자랑합니다. 이오스 섬에서는 산토리니의 아름다운 자연 경관과 전통적인 마을을 즐기면서도, 다른 관광객들과의 접촉을 최소화할 수 있습니다.")

elif st.session_state.step == "A-1.b":
   st.success("📍 **에로스 비치** 🐬")
   st.write("관능적인 사랑과 욕망의 그리스 신 이름을 딴 에로스 비치는 자연히 산토리니에서 가장 로맨틱한 곳이랍니다. 남쪽 해안에 위치하고 블리차다 비치와 가깝기 때문에 하나의 해안으로 치는 경우가 많아요. 산토리니의 전형적인 검은 자갈 모래를 볼 수 있지만 새하얀 절벽이 배경으로 펼쳐져요. 피라에서 약 10km 떨어진 비포장도로의 끝에 있고, 대중교통 노선이 없기 때문에 조용하고 한적한 곳이에요. 블리차다 비치에는 고급 비치 클럽이 있지만 에로스 비치에는 모래와 열린 공간만이 펼쳐지죠. ")

elif st.session_state.step == "A-2.a":
    st.success("📍 **이아 마을** ⚓")
    st.image("https://cdn.pixabay.com/photo/2016/11/29/04/17/santorini-1867275_1280.jpg", caption="이아 마을의 아름다운 풍경")
    st.write("산토리니에서 가장 유명한 마을 중 하나로, 화려한 건축물과 전통적인 카페, 레스토랑이 가득한 관광 명소입니다. 이아 마을은 산토리니의 아름다운 자연 경치를 360도로 감상할 수 있는 전망대와 함께, 전통적인 그리스 요리를 즐길 수 있는 다양한 레스토랑과 카페가 있는 산토리니의 유명한 랜드마크입니다.")
    
     
elif st.session_state.step == "A-2.b":
    st.success("📍 **레드비치** 🏖️")
    st.write("레드 비치는 청록빛의 맑은 바닷물이 우뚝 솟아 있는 붉은빛 바위 절벽을 감싸고 있는 아름다운 경치 때문에 산토리니에서 가장 인기 있는 해변 중 하나예요. 남쪽 해안에 위치한 이곳은 이 섬에서 유일하게 두드러지는 색감을 자랑합니다. 레드 비치의 붉은색은 바위 절벽의 색깔에서 비롯된 것으로, 이 해변은 산토리니의 대표적인 관광 명소 중 하나입니다.")

elif st.session_state.step == "B-1.a":
    st.success("📍 **세례제 요한 성 교회** ⛪")
    st.write("아름다운 교회, 흥미로운 예술 작품. 매우 평화롭고 앉아서 기도하는 소리가 느껴진다는 평가를 받는 산토리니의 상직적인 많은 종교적 그림과 미술 작품이 있는 산토리니의 유명한 성당 중 하나입니다.")
 
     
elif st.session_state.step == "B-1.b":
    st.success("📍 **산토리니 와이너리** 🍷")
    st.write("산토리니 와이너리는 산토리니 섬의 대표적인 와이너리로, 산토리니의 아름다운 자연 경관과 함께 전통적인 와인 제조 기술을 바탕으로 한 고급 와인을 생산합니다. 화산 토양 떄문에 와인 맛이 독특하고 노을보며 먹으면 분위기, 감섬까지 다 챙기는 산토리니의 숨은 보석입니다.")

     
elif st.session_state.step == "B-2.a":
    st.success("📍 **산토리니 아크로티리** 🏛️")
    st.write("아크로티리는 청동기 시대에 번성했던 미노아 문명의 일부분으로 여겨지며, 기원전 17세기경의 대화산 폭발로 인해 화산재에 매몰되면서 보존 상태가 매우 뛰어납니다. 이곳은 ‘그리스의 폼페이’라고 불리기도 하는데, 정교한 벽화, 건축물, 거리 구조 등이 잘 보존되어 당시 도시의 생활상을 살펴볼 수 있습니다. 아크로티리 발굴지에서는 집의 벽화, 도자기, 도구 등을 통해 당대 주민들의 문화와 예술, 무역 활동에 관한 많은 정보를 얻을 수 있습니다..")
      
     
elif st.session_state.step == "B-2.b":
    st.success("📍 **산토리니 화산섬** 🌋")
    st.write("산토리니 화산섬은 산토리니 섬의 중심부에 위치한 화산섬으로, 케이블카나 당나귀를 타고 투어할 수 있으며 1시간 정도 소요됩니다. 산토리니 화산섬은 산토리니의 아름다운 자연 경관과 함께, 산토리니 섬이 탄생한 3600만년 전의 화산 폭발의 흔적을 볼 수 있는 산토리니의 유명한 랜드마크입니다.")
       
      

