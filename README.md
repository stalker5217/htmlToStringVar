# html to string

innerHtml 속성을 많이 사용하는 코드에서, 수십 수백줄의 html 태그를 js 변수로 만드는게 힘들어서 만들었습니다.  

html 내용을 input.txt에 넣고 돌립니다.

input.txt
``` html
<div>
  hello world
</div>
```

output.txt
``` javascript
let html = '';
html += '<div>';
html += '  hello world';
html += '</div>;
```
