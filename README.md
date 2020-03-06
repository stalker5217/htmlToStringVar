html 동적 삽입을 위해 string 변수로 만들 때 사용합니다

``` html
<div>
  hello world
</div>
```
To

``` javascript
let html = '';
html += '<div>';
html += '  hello world';
html += '</div>;
```
