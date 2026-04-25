let currentCountryCode = null;

const card = document.querySelector('.card');
const backButton = document.querySelectorAll('.close-btn');
const graphDatas = document.querySelector('.graph-datas');
const explanationButton = document.getElementById('explanation-button');
const ai_explanation = document.getElementById('ai-explanation');
const common_data_card = document.getElementById('common-data-card');
const openCommonButton = document.getElementById('open-common-btn');

const metricMap = {
  'exchange-rate': 'exchange_rate',
  'equity-index': 'equity_index',
  'consumer-price': 'consumer_price',
  'news-sentiment': 'news_sentiment',
};

// 기본적인 지도 불려오기 
const map = new jsVectorMap({
  selector: '#map',
  map: 'world',

  // 해당 나라 클릭시 나라 코드 불러오기
  onRegionClick: async function(event, code) {
    const countryName = document.querySelector('.country-name');
    const regionNames = new Intl.DisplayNames(['en'], { type: 'region' });

    ai_explanation.classList.remove('active');
    ai_explanation.textContent = '';

    countryName.textContent = regionNames.of(code);
    // 카드 형태의 나라 정보 띄우기
    card.classList.add('active');

    currentCountryCode = code;
    // exchange_rate 그래프를 default으로 보여주는 것이 좋을 것 같음. 하지만 상의 해보기
    drawGraph(code, 'exchange_rate');
    resize();
  },

  // jsVectorMap에서 지도 다 로드되고 나서 실행되는 콜백 함수, mapInstance: 생성된 지도 객체
  onLoaded(mapInstance) {
    window.addEventListener('resize', () => {
      mapInstance.updateSize();
    });
  }
});

// 카드 형태 나라 정보 닫기
backButton.forEach((btn)=> {
  btn.addEventListener('click', (e)=> {
    const parentCard = e.target.closest('.card');

    if (parentCard) {
      parentCard.classList.remove('active');
    }
    resize();
  })
});

// 버튼 별로 다른 그래프 불러오기
graphDatas.addEventListener('click', (event)=> {
  // 버튼이 들어 왔는지 확인하기 
  if (event.target.tagName !== 'BUTTON') return;
  if (!currentCountryCode) return;
  
  const name = event.target.className;
  const metric = metricMap[name];
  if (!metric) return;
  drawGraph(currentCountryCode, metric);
});

// 버튼 클릭시 ai explanation 나오게 
explanationButton.addEventListener('click',()=> {
  if (!currentCountryCode) return;
  // 버튼 누르면 close 버튼으로 text가 변경되어서 ai explanation을 닫을 수 있는 기능을 추가할 필요가 없을 것 같음
  ai_explanation.classList.add('active');
  explanation(currentCountryCode);
  });

  // 버튼 클릭시 global indicators 나오게
openCommonButton.addEventListener('click', ()=> {
  common_data_card.classList.add('active');

  drawGlobalGraph();
  resize();
});

function resize(){
  // 카드폭 바뀌는 css 때문에, 한 박자 늦춤 
  setTimeout(() => {
    map.updateSize();
  }, 0);
}