const map = new jsVectorMap({
  selector: '#map',
  map: 'world',

  onRegionClick(event, code) {
    const card = document.querySelector('.card');
    const countryName = document.querySelector('.country-name');
    const regionNames = new Intl.DisplayNames(['en'], { type: 'region' });

    countryName.textContent = regionNames.of(code);
    card.classList.add('active');

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

function resize(){
  // 카드폭 바뀌는 css 때문에, 한 박자 늦춤 
  setTimeout(() => {
  map.updateSize();
}, 0);
}
