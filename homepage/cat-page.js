document.addEventListener('DOMContentLoaded', function () {
    const pipImage = document.getElementById('hidden-pip');
    const monotonTitlePip = document.querySelector('.monotonTitelPip');
    const abuImage = document.getElementById('hidden-abu');
    const monotonTitleAbu = document.querySelector('.monotonTitelAbu');

    // ✅ Show hidden DIV on hover
    pipImage.addEventListener('mouseover', function handleMouseOver() {
        monotonTitlePip.style.visibility = 'visible';
    });

    // ✅ (optionally) Hide DIV on mouse out
    pipImage.addEventListener('mouseout', function handleMouseOut() {
        // 👇️ if you used visibility property to hide div
        monotonTitlePip.style.visibility = 'hidden';
    });

    abuImage.addEventListener('mouseover', function handleMouseOver() {
        monotonTitleAbu.style.visibility = 'visible';
    });

    // ✅ (optionally) Hide DIV on mouse out
    abuImage.addEventListener('mouseout', function handleMouseOut() {
        // 👇️ if you used visibility property to hide div
        monotonTitleAbu.style.visibility = 'hidden';
    });
});
