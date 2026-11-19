'use strict';

// Only authored examples and drawing logic; all timing comes from script.json.
const fadeScene = S => clamp(S.u / .6) * clamp((S.d - S.u) / .5);
function heading(en, zh, a) {
  txt(en, 960, 210, {size: 49, fam: F.disp, align: 'center', w: 700, a});
  txt(zh, 960, 266, {size: 31, fam: F.zh, align: 'center', c: C.cyan, a});
}
function formula(s, x, y, size, a, c = C.white) {
  txt(s, x, y, {size, fam: F.math, align: 'center', a, c});
}
function residueRow(n, r, start, x, y, width, reveal, a) {
  const gap = width / n;
  for (let j = 0; j < n; j++) {
    const k = start + j, hit = BigInt(k) ** BigInt(r) % BigInt(n) === 0n;
    const aa = a * clamp(reveal * n - j + .5);
    chip(x + (j + .5) * gap, y, gap - 9, 65, String(k), hit ? C.mag : C.dim, aa, 25);
    if (hit) formula('−1', x + (j + .5) * gap, y + 75, 26, aa, C.mag);
  }
}

SCENES.question = S => {
  const a = fadeScene(S);
  badgeQ(S, [[0, null, 'computed']]);
  heading('AN INTEGRAL MEETS DIVISIBILITY', '一个积分，遇见整除', a);
  panel(140, 330, 760, 400, a, C.cyan, 'POLYNOMIAL / 多项式');
  formula('n = 4', 520, 408, 52, a);
  formula('T₅(x) = 16x⁵ − 20x³ + 5x', 520, 495, 37, at(S, 1, .8) * a);
  formula('I₅ = 1/6     numerator = +1', 520, 610, 38, at(S, 1, .8) * a);
  panel(1020, 330, 760, 400, a, C.mag, 'SIGN FLIPS / 符号翻转');
  residueRow(4, 4, 1, 1080, 450, 640, at(S, 2, 2.5), a);
  formula('(−1) × (−1) = +1', 1400, 650, 43, at(S, 2, 2.5) * a);
};

SCENES.detector = S => {
  const a = fadeScene(S);
  badgeQ(S, [[0, null, 'argued']]);
  heading('A FLOOR DIFFERENCE IS A SWITCH', '跨过整数，开关才亮', a);
  panel(160, 320, 1600, 190, a, C.cyan, 'EXACT INTEGER DETECTOR');
  formula('δₙ(t) = ⌊t/n⌋ − ⌊(t−1)/n⌋', 960, 400, 53, a);
  formula('δₙ(t) = 1 if n divides t;  0 otherwise', 960, 465, 34, at(S, 1, .7) * a);
  const shown = at(S, 1, .7) * a;
  panel(160, 550, 740, 220, shown, C.mag, 'HIT: n = 4, t = 8');
  formula('⌊8/4⌋ − ⌊7/4⌋ = 2 − 1 = 1', 530, 641, 33, shown);
  formula('1 − 2δ = −1', 530, 723, 39, at(S, 2, .7) * a, C.mag);
  panel(1020, 550, 740, 220, shown, C.cyan, 'MISS: n = 4, t = 9');
  formula('⌊9/4⌋ − ⌊8/4⌋ = 2 − 2 = 0', 1390, 641, 33, shown);
  formula('1 − 2δ = +1', 1390, 723, 39, at(S, 2, .7) * a);
};

SCENES.count = S => {
  const a = fadeScene(S);
  badgeQ(S, [[0, null, 'argued'], [1, 'For twelve', 'computed'], [2, null, 'argued']]);
  heading('COUNT MULTIPLES, NOT HUGE POWERS', '数倍数，不计算巨大的幂', a);
  formula('n divides kⁿ  ⇔  rad(n) divides k', 960, 355, 44, a);
  formula('12 = 2² × 3     rad(12) = 2 × 3 = 6', 960, 445, 41, at(S, 1, .7) * a);
  residueRow(12, 12, 1, 160, 555, 1600, at(S, 1, 4), a);
  formula('12 / 6 = 2 successes     (−1)² = +1', 960, 765, 41, at(S, 2, .8) * a);
};

SCENES.integral = S => {
  const a = fadeScene(S);
  badgeQ(S, [[0, null, 'argued']]);
  heading('ENDPOINT COSINES REPEAT IN FOUR STEPS', '端点余弦，四步一个周期', a);
  formula('Tₘ(cos θ) = cos(mθ)', 960, 360, 53, a);
  const b = at(S, 1, .8) * a;
  panel(260, 410, 1400, 160, b, C.cyan, 'cos(jπ/2)');
  [1, 0, -1, 0].forEach((v, j) => {
    chip(500 + j * 305, 497, 185, 72, String(v), C.cyan, b, 43, F.math);
  });
  const z = at(S, 2, .8) * a;
  formula('Iₘ = −1/(m²−1)     m even, m ≥ 2', 960, 635, 36, z);
  formula('Iₘ = 1/(m+1)     m ≡ 1 (mod 4)', 960, 695, 36, z);
  formula('Iₘ = −1/(m−1)     m ≡ 3 (mod 4)', 960, 755, 36, z);
  formula('a(n+1) = +1 exactly when 4 divides n', 960, 825, 36, z, C.cyan);
};

SCENES.powers = S => {
  const a = fadeScene(S);
  badgeQ(S, [[0, null, 'argued'], [1, null, 'computed'], [2, null, 'argued']]);
  heading('A DIFFERENT COUNT CAN KEEP THE SAME SIGN', '数量变了，奇偶性可以不变', a);
  formula('n = 16 = 2⁴', 960, 344, 46, a);
  txt('r = 2: multiples of 4', 180, 418, {size: 30, fam: F.disp, a});
  residueRow(16, 2, 1, 160, 475, 1600, at(S, 1, 2), a);
  txt('r = 4: multiples of 2', 180, 627, {size: 30, fam: F.disp, a});
  residueRow(16, 4, 1, 160, 684, 1600, at(S, 1, 2, 3), a);
  formula('4 successes → +1     8 successes → +1', 960, 805, 39, at(S, 2, .7) * a);
};

SCENES.close = S => {
  const a = fadeScene(S);
  badgeQ(S, [[0, null, 'computed'], [1, 'both equalities', 'lean'], [2, null, 'argued']]);
  heading('SHIFT THE BLOCK; KEEP THE COUNT', '平移区间，保留计数', a);
  const intro = 1 - at(S, 1, .6);
  residueRow(16, 2, -7, 160, 424, 1600, 1, a * intro);
  formula('−7, …, 8:  −4, 0, 4, 8 succeed', 960, 600, 44, a * intro);
  const exact = at(S, 1, .6) * a;
  panel(210, 320, 1500, 275, exact, C.cyan, 'BROWNE’S ORIGINAL IDENTITY · n ≥ 1');
  formula('a(n+1) = Pₙ(n;0)', 960, 425, 49, exact);
  formula('Pₙ(n;0) = (−1)^[n/rad(n)]', 960, 515, 49, exact);
  txt('Haobo Ma · Wenlin Zhang', 960, 665, {size: 35, fam: F.disp, align: 'center', a: exact});
  txt('Written extensions: arbitrary powers and integer shifts', 960, 724, {size: 31, fam: F.disp, align: 'center', c: C.dim, a: exact});
  formula('r = 1: product = −1 for every n', 960, 821, 36, at(S, 2, .6) * a, C.argued);
};

FILM.poster = () => {
  ctx.fillStyle = C.bg; ctx.fillRect(0, 0, W, H);
  heading('TWO FLOORS, ONE SIGN FLIP', '两个取整，一次符号翻转', 1);
  formula('⌊t/n⌋ − ⌊(t−1)/n⌋', 960, 391, 74, 1);
  residueRow(12, 12, 1, 160, 546, 1600, 1, 1);
  formula('divisibility → count → parity', 960, 753, 51, 1, C.cyan);
  txt('Chebyshev numerators · Browne’s identity', 960, 861, {size: 36, fam: F.disp, align: 'center'});
  txt('Haobo Ma · Wenlin Zhang', 960, 934, {size: 29, fam: F.disp, align: 'center', c: C.dim});
};
