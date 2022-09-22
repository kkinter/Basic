// 한번 만들고 다른 값을 할당하지 않기 때문에
const ajax = new XMLHttpRequest();
const NEWS_URL = 'https://api.hnpwa.com/v0/news/1.json'
ajax.open('GET', NEWS_URL , false);
ajax.send();

// console.log(ajax.response);
// Preview 탭에서 보여주는 값을 객체라고 함.
// Json 형식이기 때문에, 객체로 바꿔주는 게 가능
// 반환
const newsFeed = JSON.parse(ajax.response);
const ul = document.createElement('ul');

for(let i = 0; i < 10; i++) {
  const li = document.createElement('li');
  const a = document.createElement('a');
  // href 를 추가해주지 않으면 링크가 안됨
  a.href = '#';
  a.innerHTML = `${newsFeed[i].title} (${newsFeed[i].comments_count})`;

  li.appendChild(a);
  ul.appendChild(li);
}

document.getElementById('root').appendChild(ul);

// 문자열을 만들 때 백틱 방식을 사용
// document.getElementById('root').innerHTML =
// `<ul>
//   <li>${newsFeed[0].title}</li>
//   <li>${newsFeed[1].title}</li>
//   <li>${newsFeed[2].title}</li>
// </ul>`;

