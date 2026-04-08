let currentCountryCode = null;

const map = new jsVectorMap({
  selector: '#map',
  map: 'world',

  onRegionClick: async function(event, code) {
    const card = document.querySelector('.card');
    const countryName = document.querySelector('.country-name');
    const regionNames = new Intl.DisplayNames(['en'], { type: 'region' });
    
    countryName.textContent = regionNames.of(code);
    card.classList.add('active');

    currentCountryCode = code;
    // exchange_rate 그래프를 default으로 보여주는 것이 좋을 것 같음
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

const card = document.querySelector('.card');
const backButton = document.getElementById('back-button');
backButton.addEventListener('click', ()=>{
  card.classList.remove('active')
  resize()
});

// const exchange_rate = document.querySelector('.exchange-rate');
// const oil_price = document.querySelector('.oil-price');
// const dollar_index = document.querySelector('.dollar-index');
// const vix = document.querySelector('.vix');

const graphDatas = document.querySelector('.graph-datas');
graphDtas.addEventListener('click', (event)=> {
  // 버튼이 들어 왔는지 확인하기 
  const metric = event.target.classList[0]
  drawGraph(currentCountryCode, `${metric}`);
});

function resize(){
  // 카드폭 바뀌는 css 때문에, 한 박자 늦춤 
  setTimeout(() => {
  map.updateSize();
}, 0);
}
