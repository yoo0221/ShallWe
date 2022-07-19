$(function(){
    areaSelectMaker("select[name=addressRegion]");
});

var areaSelectMaker = function(target){
    if(target == null || $(target).length == 0){
        console.warn("Unkwon Area Tag");
        return;
    }

    var area = {
        "서울특별시": {
            "강남구": [
                "신사동",
                "논현1동",
                "논현2동",
                "압구정동",
                "청담동",
                "삼성1동",
                "삼성2동",
                "대치1동",
                "대치2동",
                "대치4동",
                "역삼1동",
                "역삼2동",
                "도곡1동",
                "도곡2동",
                "개포1동",
                "개포2동",
                "개포4동",
                "세곡동",
                "일원본동",
                "일원1동",
                "일원2동",
                "수서동"
            ],
            "강동구": [
                "강일동",
                "상일1동",
                "상일2동",
                "명일1동",
                "명일2동",
                "고덕1동",
                "고덕2동",
                "암사1동",
                "암사2동",
                "암사3동",
                "천호1동",
                "천호2동",
                "천호3동",
                "성내1동",
                "성내2동",
                "성내3동",
                "길동",
                "둔촌1동",
                "둔촌2동"
            ],
            "강북구": [
                "삼양동",
                "미아동",
                "송중동",
                "송천동",
                "삼각산동",
                "번1동",
                "번2동",
                "번3동",
                "수유1동",
                "수유2동",
                "수유3동",
                "우이동",
                "인수동"
                ],
            "강서구": [
                "염창동",
                "등촌1동",
                "등촌2동",
                "등촌3동",
                "화곡1동",
                "화곡2동",
                "화곡3동",
                "화곡4동",
                "화곡본동",
                "화곡6동",
                "화곡8동",
                "가양1동",
                "가양2동",
                "가양3동",
                "발산1동",
                "우장산동",
                "공항동",
                "방화1동",
                "방화2동",
                "방화3동"
            ],
            "관악구": [
                "보라매동",
                "청림동",
                "성현동",
                "행운동",
                "낙성대동",
                "청룡동",
                "은천동",
                "중앙동",
                "인헌동",
                "남현동",
                "서원동",
                "신원동",
                "서림동",
                "신사동",
                "신림동",
                "난향동",
                "조원동",
                "대학동",
                "삼성동",
                "미성동",
                "난곡동"
            ],
            "광진구": [
                "화양동",
                "군자동",
                "중곡1동",
                "중곡2동",
                "중곡3동",
                "중곡4동",
                "능동",
                "광장동",
                "자양1동",
                "자양2동",
                "자양3동",
                "자양4동",
                "구의1동",
                "구의2동",
                "구의3동"
            ],
            "구로구": [
                "신도림동",
                "구로1동",
                "구로2동",
                "구로3동",
                "구로4동",
                "구로5동",
                "가리봉동",
                "고척1동",
                "고척2동",
                "개봉1동",
                "개봉2동",
                "개봉3동",
                "오류1동",
                "오류2동",
                "수궁동",
                "항동"
            ],
            "금천구": [
                "가산동",
                "독산1동",
                "독산2동",
                "독산3동",
                "독산4동",
                "시흥1동",
                "시흥2동",
                "시흥3동",
                "시흥4동",
                "시흥5동",
            ],
            "노원구": [
                "월계1동",
                "월계2동",
                "월계3동",
                "공릉1동",
                "공릉2동",
                "하계1동",
                "하계2동",
                "중계본동",
                "중계1동",
                "중계4동",
                "중계2.3동",
                "상계1동",
                "상계2동",
                "상계3.4동",
                "상계5동",
                "상계6.7동",
                "상계8동",
                "상계9동",
                "상계10동"
            ],
            "도봉구": [
                "창1동",
                "창2동",
                "창3동",
                "창4동",
                "창5동",
                "도봉1동",
                "도봉2동",
                "쌍문1동",
                "쌍문2동",
                "쌍문3동",
                "쌍문4동",
                "방학1동",
                "방학2동",
                "방학3동"
            ],
            "동대문구": [
                "용신동",
                "제기동",
                "전농1동",
                "전농2동",
                "답십리1동",
                "답십리2동",
                "장안1동",
                "장안2동",
                "청량리동",
                "회기동",
                "휘경1동",
                "휘경2동",
                "이문1동",
                "이문2동"
            ],
            "동작구": [
                "노량진1동",
                "노량진2동",
                "상도1동",
                "상도2동",
                "상도3동",
                "상도4동",
                "흑석동",
                "사당1동",
                "사당2동",
                "사당3동",
                "사당4동",
                "사당5동",
                "대방동",
                "신대방1동",
                "신대방2동"
            ],
            "마포구": [
                "아현동",
                "공덕동",
                "도화동",
                "용강동",
                "대흥동",
                "염리동",
                "신수동",
                "서강동",
                "서교동",
                "합정동",
                "망원1동",
                "망원2동",
                "연남동",
                "성산1동",
                "성산2동",
                "상암동"
            ],
            "서대문구": [
                "천연동",
                "북아현동",
                "충현동",
                "신촌동",
                "연희동",
                "홍제1동",
                "홍제3동",
                "홍제2동",
                "홍은1동",
                "홍은2동",
                "남가좌1동",
                "남가좌2동",
                "북가좌1동",
                "북가좌2동"
            ],
            "서초구": [
                "서초1동",
                "서초2동",
                "서초3동",
                "서초4동",
                "잠원동",
                "반포본동",
                "반포1동",
                "반포2동",
                "반포3동",
                "반포4동",
                "방배본동",
                "방배1동",
                "방배2동",
                "방배3동",
                "방배4동",
                "양재1동",
                "양재2동",
                "내곡동"
            ],
            "성동구": [
                "왕십리2동",
                "왕십리도선동",
                "마장동",
                "사근동",
                "행당1동",
                "행당2동",
                "응봉동",
                "금호1가동",
                "금호2.3가동",
                "금호4가동",
                "옥수동",
                "성수1가1동",
                "성수1가2동",
                "성수2가1동",
                "성수2가3동",
                "송정동",
                "용답동"
            ],
            "성북구": [
                "성북동",
                "삼선동",
                "동선동",
                "돈암1동",
                "돈암2동",
                "안암동",
                "보문동",
                "정릉1동",
                "정릉2동",
                "정릉3동",
                "정릉4동",
                "길음1동",
                "길음2동",
                "종암동",
                "월곡1동",
                "월곡2동",
                "장위1동",
                "장위2동",
                "장위3동",
                "석관동"
            ],
            "송파구": [
                "풍납1동",
                "풍납2동",
                "거여1동",
                "거여2동",
                "마천1동",
                "마천2동",
                "방이1동",
                "방이2동",
                "오륜동",
                "오금동",
                "송파1동",
                "송파2동",
                "석촌동",
                "삼전동",
                "가락본동",
                "가락1동",
                "가락2동",
                "문정1동",
                "문정2동",
                "장지동",
                "위례동",
                "잠실본동",
                "잠실2동",
                "잠실3동",
                "잠실4동",
                "잠실6동",
                "잠실7동"
            ],
            "양천구": [
                "목1동",
                "목2동",
                "목3동",
                "목4동",
                "목5동",
                "신월1동",
                "신월2동",
                "신월3동",
                "신월4동",
                "신월5동",
                "신월6동",
                "신월7동",
                "신정1동",
                "신정2동",
                "신정3동",
                "신정4동",
                "신정6동",
                "신정7동"
            ],
            "영등포구": [
                "영등포본동",
                "영등포동",
                "여의동",
                "당산1동",
                "당산2동",
                "도림동",
                "문래동",
                "양평1동",
                "양평2동",
                "신길1동",
                "신길3동",
                "신길4동",
                "신길5동",
                "신길6동",
                "신길7동",
                "대림1동",
                "대림2동",
                "대림3동"
            ],
            "용산구": [
                "후암동",
                "용산2가동",
                "남영동",
                "청파동",
                "원효로1동",
                "원효로2동",
                "효창동",
                "용문동",
                "한강로동",
                "이촌1동",
                "이촌2동",
                "이태원1동",
                "이태원2동",
                "한남동",
                "서빙고동",
                "보광동"
            ],
            "은평구": [
                "녹번동",
                "불광1동",
                "불광2동",
                "갈현1동",
                "갈현2동",
                "구산동",
                "대조동",
                "응암1동",
                "응암2동",
                "응암3동",
                "역촌동",
                "신사1동",
                "신사2동",
                "증산동",
                "수색동",
                "진관동"
            ],
            "종로구": [
                "청운효자동",
                "사직동",
                "삼청동",
                "부암동",
                "평창동",
                "무악동",
                "교남동",
                "가회동",
                "종로1.2.3.4가동",
                "종로5.6가동",
                "이화동",
                "혜화동",
                "창신1동",
                "창신2동",
                "창신3동",
                "숭인1동",
                "숭인2동"
            ],
            "중구": [
                "소공동",
                "회현동",
                "명동",
                "필동",
                "장충동",
                "광희동",
                "을지로동",
                "신당동",
                "다산동",
                "약수동",
                "청구동",
                "신당5동",
                "동화동",
                "황학동",
                "중림동"
            ],
            "중랑구": [
                "면목2동",
                "면목4동",
                "면목5동",
                "면목본동",
                "면목7동",
                "면목3.8동",
                "상봉1동",
                "상봉2동",
                "중화1동",
                "중화2동",
                "묵1동",
                "묵2동",
                "망우본동",
                "망우3동",
                "신내1동",
                "신내2동"
            ]
        },
        "부산광역시": {
            "강서구": [
                "대저1동",
                "대저2동",
                "강동동",
                "명지1동",
                "명지2동",
                "가락동",
                "녹산동",
                "가덕도동",
            ],
            "금정구": [
                "서1동",
                "서2동",
                "서3동",
                "금사회동동",
                "부곡1동",
                "부곡2동",
                "부곡3동",
                "부곡4동",
                "장전1동",
                "장전2동",
                "선두구동",
                "청룡노포동",
                "남산동",
                "구서1동",
                "구서2동",
                "금성동"
            ],
            "남구": [
                "대연1동",
                "대연3동",
                "대연4동",
                "대연5동",
                "대연6동",
                "용호1동",
                "용호2동",
                "용호3동",
                "용호4동",
                "용당동",
                "감만1동",
                "감만2동",
                "우암동",
                "문현1동",
                "문현2동",
                "문현3동",
                "문현4동",
            ],
            "동구": [
                "초량1동",
                "초량2동",
                "초량3동",
                "초량6동",
                "수정1동",
                "수정2동",
                "수정4동",
                "수정5동",
                "좌천동",
                "범일1동",
                "범일2동",
                "범일5동"
            ],
            "동래구": [
                "수민동",
                "복산동",
                "명륜동",
                "온천1동",
                "온천2동",
                "온천3동",
                "사직1동",
                "사직2동",
                "사직3동",
                "안락1동",
                "안락2동",
                "명장1동",
                "명장2동"
            ],
            "부산진구": [
                "부전1동",
                "부전2동",
                "연지동",
                "초읍동",
                "양정1동",
                "양정2동",
                "전포1동",
                "전포2동",
                "부암1동",
                "부암3동",
                "당감제1동",
                "당감2동",
                "당감4동",
                "가야제1동",
                "가야2동",
                "개금1동",
                "개금2동",
                "개금3동",
                "범천1동",
                "범천2동"
            ],
            "북구": [
                "구포1동",
                "구포2동",
                "구포3동",
                "금곡동",
                "화명1동",
                "화명2동",
                "화명3동",
                "덕천1동",
                "덕천2동",
                "덕천3동",
                "만덕1동",
                "만덕2동",
                "만덕3동"
            ],
            "사상구": [
                "삼락동",
                "모라1동",
                "모라3동",
                "덕포1동",
                "덕포2동",
                "괘법동",
                "감전동",
                "주례1동",
                "주례2동",
                "주례3동",
                "학장동",
                "엄궁동"
            ],
            "사하구": [
                "괴정1동",
                "괴정2동",
                "괴정3동",
                "괴정4동",
                "당리동",
                "하단1동",
                "하단2동",
                "신평1동",
                "신평2동",
                "장림1동",
                "장림2동",
                "다대1동",
                "다대2동",
                "구평동",
                "감천1동",
                "감천2동"
            ],
            "서구": [
                "동대신1동",
                "동대신2동",
                "동대신3동",
                "서대신1동",
                "서대신3동",
                "서대신4동",
                "부민동",
                "아미동",
                "초장동",
                "충무동",
                "남부민1동",
                "남부민2동",
                "암남동"
            ],
            "수영구": [
                "남천1동",
                "남천2동",
                "수영동",
                "망미1동",
                "망미2동",
                "광안1동",
                "광안2동",
                "광안3동",
                "광안4동",
                "민락동"
            ],
            "연제구": [
                "거제1동",
                "거제2동",
                "거제3동",
                "거제4동",
                "연산1동",
                "연산2동",
                "연산3동",
                "연산4동",
                "연산5동",
                "연산6동",
                "연산8동",
                "연산9동"
            ],
            "영도구": [
                "남항동",
                "영선1동",
                "영선2동",
                "신선동",
                "봉래1동",
                "봉래2동",
                "청학1동",
                "청학2동",
                "동삼1동",
                "동삼2동",
                "동삼3동"
            ],
            "중구": [
                "중앙동",
                "동광동",
                "대청동",
                "보수동",
                "부평동",
                "광복동",
                "남포동",
                "영주1동",
                "영주2동",
            ],
            "해운대구": [
                "우1동",
                "우2동",
                "우3동",
                "중1동",
                "중2동",
                "좌1동",
                "좌2동",
                "좌3동",
                "좌4동",
                "송정동",
                "반여1동",
                "반여2동",
                "반여3동",
                "반여4동",
                "반송1동",
                "반송2동",
                "재송1동",
                "재송2동"
            ],
            "기장군": [
                "기장읍",
                "장안읍",
                "정관읍",
                "일광읍",
                "철마면",
            ]
        },
        "대구광역시": {
            "남구": [
                "이천동",
                "봉덕1동",
                "봉덕2동",
                "봉덕3동",
                "대명1동",
                "대명2동",
                "대명3동",
                "대명4동",
                "대명5동",
                "대명6동",
                "대명9동",
                "대명10동",
                "대명11동"
            ],
            "달서구": [
                "성당동",
                "두류1.2동",
                "두류3동",
                "감삼동",
                "죽전동",
                "장기동",
                "용산1동",
                "용산2동",
                "이곡1동",
                "이곡2동",
                "신당동",
                "본리동",
                "월성1동",
                "월성2동",
                "진천동",
                "유천동",
                "상인1동",
                "상인2동",
                "상인3동",
                "도원동",
                "송현1동",
                "송현2동",
                "본동"
            ],
            "동구": [
                "신암1동",
                "신암2동",
                "신암3동",
                "신암4동",
                "신암5동",
                "신천1.2동",
                "신천3동",
                "신천4동",
                "효목1동",
                "효목2동",
                "도평동",
                "불로.봉무동",
                "지저동",
                "동촌동",
                "방촌동",
                "해안동",
                "안심1동",
                "안심2동",
                "안심3동",
                "안심4동",
                "혁신동",
                "공산동"
            ],
            "북구": [
                "고성동",
                "칠성동",
                "침산1동",
                "침산2동",
                "침산3동",
                "산격1동",
                "산격2동",
                "산격3동",
                "산격4동",
                "대현동",
                "복현1동",
                "복현2동",
                "검단동",
                "무태조야동",
                "관문동",
                "태전1동",
                "태전2동",
                "구암동",
                "관음동",
                "읍내동",
                "동천동",
                "노원동",
                "국우동"
            ],
            "서구": [
                "내당1동",
                "내당2.3동",
                "내당4동",
                "비산1동",
                "비산2.3동",
                "비산4동",
                "비산5동",
                "비산6동",
                "비산7동",
                "평리1동",
                "평리2동",
                "평리3동",
                "평리4동",
                "평리5동",
                "평리6동",
                "상중이동",
                "원대동"
            ],
            "수성구": [
                "범어1동",
                "범어2동",
                "범어3동",
                "범어4동",
                "만촌1동",
                "만촌2동",
                "만촌3동",
                "수성1가동",
                "수성2.3가동",
                "수성4가동",
                "황금1동",
                "황금2동",
                "중동",
                "상동",
                "파동",
                "두산동",
                "지산1동",
                "지산2동",
                "범물1동",
                "범물2동",
                "고산1동",
                "고산2동",
                "고산3동"
            ],
            "중구": [
                "동인동",
                "삼덕동",
                "성내1동",
                "성내2동",
                "성내3동",
                "대신동",
                "남산1동",
                "남산2동",
                "남산3동",
                "남산4동",
                "대봉1동",
                "대봉2동"
            ],
            "달성군": [
                "화원읍",
                "논공읍",
                "다사읍",
                "유가읍",
                "옥포읍",
                "현풍읍",
                "가창면",
                "하빈면",
                "구지면"
            ]
        },		

        "인천광역시": {
            "계양구": [
                "효성1동",
                "효성2동",
                "계산1동",
                "계산2동",
                "계산3동",
                "계산4동",
                "작전1동",
                "작전2동",
                "작전서운동",
                "계양1동",
                "계양2동",
                "계양3동"
            ],
            "미추홀구": [
                "숭의2동",
                "숭의1.3동",
                "숭의4동",
                "용현1.4동",
                "용현2동",
                "용현3동",
                "용현5동",
                "학익1동",
                "학익2동",
                "도화1동",
                "도화2.3동",
                "주안1동",
                "주안2동",
                "주안3동",
                "주안4동",
                "주안5동",
                "주안6동",
                "주안7동",
                "주안8동",
                "관교동",
                "문학동"
            ],
            "남동구": [
                "구월1동",
                "구월2동",
                "구월3동",
                "구월4동",
                "간석1동",
                "간석2동",
                "간석3동",
                "간석4동",
                "만수1동",
                "만수2동",
                "만수3동",
                "만수4동",
                "만수5동",
                "만수6동",
                "장수서창동",
                "서창2동",
                "남촌도림동",
                "논현1동",
                "논현2동",
                "논현고잔동"
            ],
            "동구": [
                "만석동",
                "화수1.화평동",
                "화수2동",
                "송현1.2동",
                "송현3동",
                "송림1동",
                "송림2동",
                "송림3.5동",
                "송림4동",
                "송림6동",
                "금창동"
            ],
            "부평구": [
                "부평1동",
                "부평2동",
                "부평3동",
                "부평4동",
                "부평5동",
                "부평6동",
                "산곡1동",
                "산곡2동",
                "산곡3동",
                "산곡4동",
                "청천1동",
                "청천2동",
                "갈산1동",
                "갈산2동",
                "삼산1동",
                "삼산2동",
                "부개1동",
                "부개2동",
                "부개3동",
                "일신동",
                "십정1동",
                "십정2동"
            ],
            "서구": [
                "검암경서동",
                "연희동",
                "청라1동",
                "청라2동",
                "청라3동",
                "가정1동",
                "가정2동",
                "가정3동",
                "석남1동",
                "석남2동",
                "석남3동",
                "신현원창동",
                "가좌1동",
                "가좌2동",
                "가좌3동",
                "가좌4동",
                "검단동",
                "불로대곡동",
                "원당동",
                "당하동",
                "오류왕길동",
                "마전동",
                "아라동"
            ],
            "연수구": [
                "옥련1동",
                "옥련2동",
                "선학동",
                "연수1동",
                "연수2동",
                "연수3동",
                "청학동",
                "동춘1동",
                "동춘2동",
                "동춘3동",
                "송도1동",
                "송도2동",
                "송도3동",
                "송도4동",
                "송도5동"
            ],
            "중구": [
                "연안동",
                "신포동",
                "신흥동",
                "도원동",
                "율목동",
                "동인천동",
                "개항동",
                "영종동",
                "영종1동",
                "운서동",
                "용유동"
            ],
            "강화군": [
                "강화읍",
                "선원면",
                "불은면",
                "길상면",
                "화도면",
                "양도면",
                "내가면",
                "하점면",
                "양사면",
                "송해면",
                "교동면",
                "삼산면",
                "서도면"
            ],
            "옹진군": [
                "북도면",
                "백령면",
                "대청면",
                "덕적면",
                "영흥면",
                "자월면",
                "연평면"
            ]
        },
        "광주광역시": {
            "광산구": [
                "송정1동",
                "송정2동",
                "도산동",
                "신흥동",
                "어룡동",
                "우산동",
                "월곡1동",
                "월곡2동",
                "비아동",
                "첨단1동",
                "첨단2동",
                "신가동",
                "운남동",
                "수완동",
                "하남동",
                "임곡동",
                "동곡동",
                "평동",
                "삼도동",
                "본량동",
                "신창동"
            ],
            "남구": [
                "양림동",
                "방림1동",
                "방림2동",
                "봉선1동",
                "봉선2동",
                "사직동",
                "월산동",
                "월산4동",
                "월산5동",
                "백운1동",
                "백운2동",
                "주월1동",
                "주월2동",
                "진월동",
                "효덕동",
                "송암동",
                "대촌동"
            ],
            "동구": [
                "충장동",
                "동명동",
                "계림1동",
                "계림2동",
                "산수1동",
                "산수2동",
                "지산1동",
                "지산2동",
                "서남동",
                "학동",
                "학운동",
                "지원1동",
                "지원2동"
            ],
            "북구": [
                "중흥1동",
                "중흥2동",
                "중흥3동",
                "중앙동",
                "임동",
                "신안동",
                "용봉동",
                "운암1동",
                "운암2동",
                "운암3동",
                "동림동",
                "우산동",
                "풍향동",
                "문화동",
                "문흥1동",
                "문흥2동",
                "두암1동",
                "두암2동",
                "두암3동",
                "삼각동",
                "일곡동",
                "매곡동",
                "오치1동",
                "오치2동",
                "석곡동",
                "건국동",
                "양산동",
                "신용동"
            ],
            "서구": [
                "양동",
                "양3동",
                "농성1동",
                "농성2동",
                "광천동",
                "유덕동",
                "치평동",
                "상무1동",
                "상무2동",
                "화정1동",
                "화정2동",
                "화정3동",
                "화정4동",
                "서창동",
                "금호1동",
                "금호2동",
                "풍암동",
                "동천동"
            ]
        },

        "대전광역시": {
            "대덕구": [
                "오정동",
                "대화동",
                "회덕동",
                "비래동",
                "송촌동",
                "중리동",
                "신탄진동",
                "석봉동",
                "덕암동",
                "목상동",
                "법1동",
                "법2동"
            ],
            "동구": [
                "중앙동",
                "효동",
                "신인동",
                "판암1동",
                "판암2동",
                "용운동",
                "대동",
                "자양동",
                "가양1동",
                "가양2동",
                "용전동",
                "성남동",
                "홍도동",
                "삼성동",
                "대청동",
                "산내동"
            ],
            "서구": [
                "복수동",
                "도마1동",
                "도마2동",
                "정림동",
                "변동",
                "용문동",
                "탄방동",
                "괴정동",
                "가장동",
                "내동",
                "갈마1동",
                "갈마2동",
                "월평1동",
                "월평2동",
                "월평3동",
                "가수원동",
                "도안동",
                "관저1동",
                "관저2동",
                "기성동",
                "둔산1동",
                "둔산2동",
                "만년동",
                "둔산3동"
            ],
            "유성구": [
                "진잠동",
                "학하동",
                "상대동",
                "온천1동",
                "온천2동",
                "노은1동",
                "노은2동",
                "노은3동",
                "신성동",
                "전민동",
                "구즉동",
                "관평동",
                "원신흥동"
            ],
            "중구": [
                "은행선화동",
                "목동",
                "중촌동",
                "대흥동",
                "문창동",
                "석교동",
                "대사동",
                "부사동",
                "용두동",
                "오류동",
                "태평1동",
                "태평2동",
                "유천1동",
                "유천2동",
                "문화1동",
                "문화2동",
                "산성동"
            ],
        },

        "울산광역시": {
            "남구": [
                "신정1동",
                "신정2동",
                "신정3동",
                "신정4동",
                "신정5동",
                "달동",
                "삼산동",
                "삼호동",
                "무거동",
                "옥동",
                "대현동",
                "수암동",
                "선암동",
                "야음장생포동"
            ],
            "동구": [
                "방어동",
                "일산동",
                "화정동",
                "대송동",
                "전하1동",
                "전하2동",
                "남목1동",
                "남목2동",
                "남목3동"
            ],
            "북구": [
                "농소1동",
                "농소2동",
                "농소3동",
                "강동동",
                "효문동",
                "송정동",
                "양정동",
                "염포동"
            ],
            "중구": [
                "학성동",
                "반구1동",
                "반구2동",
                "복산1동",
                "복산2동",
                "중앙동",
                "우정동",
                "태화동",
                "다운동",
                "병영1동",
                "병영2동",
                "약사동",
                "성안동"
            ],
            "울주군": [
                "온산읍",
                "언양읍",
                "온양읍",
                "범서읍",
                "청량읍",
                "삼남읍",
                "서생면",
                "웅촌면",
                "두동면",
                "두서면",
                "상북면",
                "삼동면"
            ],
        },
        "세종특별자치시": {
            "세종특별자치시": [
                "조치원읍",
                "연기면",
                "연동면",
                "부강면",
                "금남면",
                "장군면",
                "연서면",
                "전의면",
                "전동면",
                "소정면",
                "한솔동",
                "새롬동",
                "도담동",
                "해밀동",
                "아름동",
                "종촌동",
                "고운동",
                "소담동",
                "반곡동",
                "보람동",
                "대평동",
                "다정동"
            ],
        },
        "경기도": {
            "수원시 장안구": [
                
            ],
            "수원시 권선구": [],
            "수원시 팔달구": [],
            "수원시 영통구": [],
            "성남시 수정구": [],
            "성남시 중원구": [],
            "성남시 분당구": [],
            "의정부시": [],
            "안양시 만안구": [],
            "안양시 동안구": [],
            "부천시": [],
            "광명시": [],
            "평택시": [],
            "동두천시": [],
            "안산시 상록구": [],
            "안산시 단원구": [],
            "고양시 덕양구": [],
            "고양시 일산동구": [],
            "고양시 일산서구": [],
            "과천시": [],
            "구리시": [],
            "남양주시": [],
            "오산시": [],
            "시흥시": [],
            "군포시": [],
            "의왕시": [],
            "하남시": [],
            "용인시 처인구": [],
            "용인시 기흥구": [],
            "용인시 수지구": [],
            "파주시": [],
            "이천시": [],
            "안성시": [],
            "김포시": [],
            "화성시": [],
            "광주시": [],
            "양주시": [],
            "포천시": [],
            "여주시": [],
            "연천시": [],
            "가평시": [],
            "양평시": []
        },
        "서울특별시": {
            "강남구":["신사동",
                    "논현1동",
                    "논현2동",
                    "압구정동",
                    "청담동",
                    "삼성1동",
                    "삼성2동",
                    "대치1동",
                    "대치2동",
                    "대치4동",
                    "역삼1동",
                    "역삼2동",
                    "도곡1동",
                    "도곡2동",
                    "개포1동",
                    "개포2동",
                    "개포4동",
                    "세곡동",
                    "일원본동",
                    "일원1동",
                    "일원2동",
                    "수서동"
            ],
            "강동구": [],
            "강북구": [],
            "강서구": [],
            "관악구": [],
            "광진구": [],
            "구로구": [],
            "금천구": [],
            "노원구": [],
            "도봉구": [],
            "동대문구": [],
            "동작구": [],
            "마포구": [],
            "서대문구": [],
            "서초구": [],
            "성동구": [],
            "성북구": [],
            "송파구": [],
            "양천구": [],
            "영등포구": [],
            "용산구": [],
            "은평구": [],
            "종로구": [],
            "중구": [],
            "중랑구": []
        },
        "수도권" :{
            "서울특별시": ["강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구", "노원구", "도봉구",
                "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구", "성북구", "송파구", "양천구", "영등포구", "용산구",
                "은평구", "종로구", "중구", "중랑구"],
            "경기도" : [ "수원시 장안구", "수원시 권선구", "수원시 팔달구", "수원시 영통구", "성남시 수정구", "성남시 중원구", "성남시 분당구", "의정부시", "안양시 만안구", "안양시 동안구", "부천시", "광명시", "평택시", "동두천시", "안산시 상록구", "안산시 단원구", "고양시 덕양구", "고양시 일산동구",
                "고양시 일산서구", "과천시", "구리시", "남양주시", "오산시", "시흥시", "군포시", "의왕시", "하남시", "용인시 처인구", "용인시 기흥구", "용인시 수지구", "파주시", "이천시", "안성시", "김포시", "화성시", "광주시", "양주시", "포천시", "여주시", "연천군", "가평군",
                "양평군" ],
            "인천광역시" : [ "계양구", "미추홀구", "남동구", "동구", "부평구", "서구", "연수구", "중구", "강화군", "옹진군" ]			
        },
        "강원권" :{
            "강원도" : [ "춘천시", "원주시", "강릉시", "동해시", "태백시", "속초시", "삼척시", "홍천군", "횡성군", "영월군", "평창군", "정선군", "철원군", "화천군", "양구군", "인제군", "고성군", "양양군" ]			
        },
        "충청권" :{
            "충청북도" : [ "청주시 상당구", "청주시 서원구", "청주시 흥덕구", "청주시 청원구", "충주시", "제천시", "보은군", "옥천군", "영동군", "증평군", "진천군", "괴산군", "음성군", "단양군" ],
            "충청남도" : [ "천안시 동남구", "천안시 서북구", "공주시", "보령시", "아산시", "서산시", "논산시", "계룡시", "당진시", "금산군", "부여군", "서천군", "청양군", "홍성군", "예산군", "태안군" ],
            "대전광역시" : [ "대덕구", "동구", "서구", "유성구", "중구" ],
            "세종특별자치시" : [ "세종특별자치시" ]			
        },
        "전라권" :{
            "전라북도" : [ "전주시 완산구", "전주시 덕진구", "군산시", "익산시", "정읍시", "남원시", "김제시", "완주군", "진안군", "무주군", "장수군", "임실군", "순창군", "고창군", "부안군" ],
            "전라남도" : [ "목포시", "여수시", "순천시", "나주시", "광양시", "담양군", "곡성군", "구례군", "고흥군", "보성군", "화순군", "장흥군", "강진군", "해남군", "영암군", "무안군", "함평군", "영광군", "장성군", "완도군", "진도군", "신안군" ],
            "광주광역시" : [ "광산구", "남구", "동구", "북구", "서구" ]			
        },
        "경상권" : {
            "경상북도" : [ "포항시 남구", "포항시 북구", "경주시", "김천시", "안동시", "구미시", "영주시", "영천시", "상주시", "문경시", "경산시", "군위군", "의성군", "청송군", "영양군", "영덕군", "청도군", "고령군", "성주군", "칠곡군", "예천군", "봉화군", "울진군", "울릉군" ],
            "경상남도" : [ "창원시 의창구", "창원시 성산구", "창원시 마산합포구", "창원시 마산회원구", "창원시 진해구", "진주시", "통영시", "사천시", "김해시", "밀양시", "거제시", "양산시", "의령군", "함안군", "창녕군", "고성군", "남해군", "하동군", "산청군", "함양군", "거창군", "합천군" ],
            "부산광역시" : [ "강서구", "금정구", "남구", "동구", "동래구", "부산진구", "북구", "사상구", "사하구", "서구", "수영구", "연제구", "영도구", "중구", "해운대구", "기장군" ],
            "대구광역시" : [ "남구", "달서구", "동구", "북구", "서구", "수성구", "중구", "달성군" ],
            "울산광역시" : [ "남구", "동구", "북구", "중구", "울주군" ]			
        },
        "제주권" : {
            "제주특별자치도" : [ "서귀포시", "제주시" ]			
        }
    };

    for(i=0; i<$(target).length; i++){
        (function(z){
            var a1 = $(target).eq(z);
            var a2 = a1.next();
            var a3 = a2.next();

            //초기화
            init(a1, true);

            //권역 기본 생성
            var areaKeys1 = Object.keys(area);
            areaKeys1.forEach(function(Region){
                a1.append("<option value="+Region+">"+Region+"</option>");
            });

            //변경 이벤트
            $(a1).on("change", function(){
                init($(this), false);
                var Region = $(this).val();
                var keys = Object.keys(area[Region]);
                keys.forEach(function(Do){
                    a2.append("<option value="+Do+">"+Do+"</option>");    
                });
            });

            $(a2).on("change", function(){
                a3.empty().append("<option value=''>선택</option>");
                var Region = a1.val();
                var Do = $(this).val();
                var keys = Object.keys(area[Region][Do]);
                keys.forEach(function(SiGunGu){
                    a3.append("<option value="+area[Region][Do][SiGunGu]+">"+area[Region][Do][SiGunGu]+"</option>");    
                });
            });
        })(i);        

        function init(t, first){
            first ? t.empty().append("<option value=''>선택</option>") : "";
            t.next().empty().append("<option value=''>선택</option>");
            t.next().next().empty().append("<option value=''>선택</option>");
        }
    }
}