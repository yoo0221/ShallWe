'use strict';
const toast = document.getElementById('toast');  // id가 toast인 요소 div
        let isToastShown = false;
        // id가 toastButton인 요소를 클릭하면 아래 함수가 호출됨
        document.getElementById('toastButton').addEventListener('click', function () {
            if (isToastShown) return;   // 토스트 메시지가 띄어져 있다면 함수를 끝냄
            isToastShown = true;
            toast.classList.add('show');    // show라는 클래스를 추가해서 토스트 메시지를 띄우는 애니메이션을 발동시킴
            setTimeout(function () {
                // 2700ms 후에 show 클래스를 제거함
                toast.classList.remove('show');
                isToastShown = false;
            }, 2700);
        });