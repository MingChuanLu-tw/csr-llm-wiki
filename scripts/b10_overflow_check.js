/* B10 render check — overflow over every slide, backups included.
 *
 * Run against a REAL HTTP origin (log.md:176 — a data: snapshot never runs the
 * JS or loads KaTeX, so a check against one certifies nothing):
 *     cd slides_html && python3 -m http.server 8731
 * then execute this file's contents in the page.
 *
 * Criterion, vertical: every non-absolutely-positioned child of a slide must end
 * above that slide's .foot. .foot and .n are absolute chrome living in the stage
 * padding, so a padding-box criterion reports all 37 slides as failing.
 * Criterion, horizontal: scrollWidth must not exceed clientWidth. Do NOT use
 * offsetLeft+offsetWidth on inline elements — a wrapped inline reports its union
 * box and produces false positives (slide 8).
 */
(() => {
  const slides = [...document.querySelectorAll('section.slide')];
  const prevOn = slides.map(s => s.classList.contains('on'));
  const rows = [];
  slides.forEach((s, i) => {
    slides.forEach(x => x.classList.remove('on'));
    s.classList.add('on');
    void s.offsetHeight;                                  // force layout
    const foot = s.querySelector('.foot');
    const limit = foot ? foot.offsetTop : s.offsetHeight;
    let over = -Infinity, who = '';
    [...s.children].forEach(el => {
      const pos = getComputedStyle(el).position;
      if (pos === 'absolute' || pos === 'fixed') return;   // chrome, not content
      const bottom = el.offsetTop + el.offsetHeight;
      if (bottom - limit > over) { over = bottom - limit; who = el.tagName + '.' + el.className; }
    });
    rows.push({
      slide: i + 1,
      overBottom: +over.toFixed(1),
      culprit: who,
      overRight: s.scrollWidth - s.clientWidth,
      overScroll: s.scrollHeight - s.clientHeight,
    });
  });
  slides.forEach((x, i) => x.classList.toggle('on', prevOn[i]));
  const bad = rows.filter(r => r.overBottom > 0.5 || r.overRight > 0.5 || r.overScroll > 0.5);
  return {
    stage: { w: slides[0].offsetWidth, h: slides[0].offsetHeight },
    total: rows.length,
    failing: bad.length,
    failures: bad,
    tightestClearance: Math.max(...rows.map(r => r.overBottom)).toFixed(1),
  };
})()
