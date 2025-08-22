document.addEventListener('DOMContentLoaded', () => {
    const fontSelector = document.getElementById('font-selector');
    const increaseFontSizeButton = document.getElementById('increase-font-size');
    const decreaseFontSizeButton = document.getElementById('decrease-font-size');
    const fontColorSelector = document.getElementById('font-color-selector');
    const invertColorButton = document.getElementById('invert-color');

    let currentFontSize = 16;
    let isInverted = false;

    // Change font
    fontSelector.addEventListener('change', () => {
        const selectedFont = fontSelector.value;

        if (selectedFont === 'opendyslexic') {
            document.body.style.fontFamily = '"OpenDyslexic", sans-serif';
        } else if (selectedFont === 'times-new-roman') {
            document.body.style.fontFamily = '"Times New Roman", sans-serif';
        }
		else if (selectedFont === 'arial') {
            document.body.style.fontFamily = '"Arial", sans-serif';
        }

        document.querySelectorAll('h1, h2, h3, h4, h5, h6').forEach(el => {
            el.style.fontFamily = selectedFont;
        });
    });

    // Change text size
    increaseFontSizeButton.addEventListener('click', () => {
        if (currentFontSize < 32) {
            currentFontSize += 2;
            document.body.style.fontSize = currentFontSize + 'px';
            document.querySelectorAll('h1, h2, h3, h4, h5, h6').forEach(el => {
                el.style.fontSize = el.style.fontSize + 'px';
            });
        };
    });

    decreaseFontSizeButton.addEventListener('click', () => {
        currentFontSize = Math.max(12, currentFontSize - 2);
        document.body.style.fontSize = currentFontSize + 'px';
        document.querySelectorAll('h1, h2, h3, h4, h5, h6').forEach(el => {
            el.style.fontSize = el.style.fontSize + 'px';
        });
    });

    // Change text color
    fontColorSelector.addEventListener('input', (event) => {
        const selectedColor = event.target.value;
        document.body.style.color = selectedColor;
        document.querySelectorAll('p, h1, h2, h3, h4, h5, h6').forEach(el => {
            el.style.color = selectedColor;
        });
    });

    // Dark mode option
    invertColorButton.addEventListener('click', () => {
        if (isInverted) {
            document.body.style.backgroundColor = '#ffffff';
            document.body.style.color = '#000000';
            document.querySelectorAll('p, h1, h2, h3, h4, h5, h6').forEach(el => {
                el.style.color = '#000000';
            });
            document.querySelectorAll('td, th').forEach(el => {
            el.style.border = '';
            });
            document.querySelectorAll('tr').forEach(el => {
            el.style.backgroundColor = '';
            });
        } else {
            document.body.style.backgroundColor = '#000000';
            document.body.style.color = '#ffffff';
            document.querySelectorAll('p, h1, h2, h3, h4, h5, h6').forEach(el => {
                el.style.color = '#ffffff';
            });
            document.querySelectorAll('td, th').forEach(el => {
            el.style.border = '1px solid #ffffff';
            });
            document.querySelectorAll('tr').forEach(el => {
            el.style.backgroundColor = '#000000';
            });
        }
        isInverted = !isInverted;
    });
});
