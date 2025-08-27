// 新版本：draggable_math.js (兼容 MathJax 3)

// MathJax 3 使用 promise 来处理加载和渲染
window.MathJax = {
  startup: {
    ready: () => {
      console.log('MathJax is ready to be configured.');
      MathJax.startup.defaultReady();
      MathJax.startup.promise.then(() => {
        console.log('MathJax has finished typesetting. Applying draggable feature.');
        const formulaBlocks = document.querySelectorAll('mjx-container[display="true"]');
        formulaBlocks.forEach(makeDraggable);
      });
    }
  }
};

function makeDraggable(element) {
  let isDragging = false;
  let offsetX, offsetY;

  // 我们需要拖拽 mjx-container 的父元素（通常是 display-style 的 div）
  const parentWrapper = element.closest('div');
  if (!parentWrapper) return;
  
  parentWrapper.classList.add('draggable');
  parentWrapper.style.position = 'relative';

  parentWrapper.addEventListener('mousedown', (e) => {
    e.preventDefault();
    isDragging = true;
    offsetX = e.clientX - parentWrapper.offsetLeft;
    offsetY = e.clientY - parentWrapper.offsetTop;
    document.body.style.userSelect = 'none';
    parentWrapper.classList.add('dragging');
  });

  document.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    parentWrapper.style.left = `${e.clientX - offsetX}px`;
    parentWrapper.style.top = `${e.clientY - offsetY}px`;
  });

  document.addEventListener('mouseup', () => {
    if (!isDragging) return;
    isDragging = false;
    document.body.style.userSelect = '';
    parentWrapper.classList.remove('dragging');
  });
}