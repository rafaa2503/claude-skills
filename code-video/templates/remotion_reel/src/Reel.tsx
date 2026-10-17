import React from "react";
import { AbsoluteFill, Audio, Img, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig, Easing } from "remotion";

const OR = "#ff9f1c", ORL = "#ffcd78", ORD = "#c66e00", WH = "#f5f5f7", GR = "#969ea8", CARD = "#13171c", EDGE = "#37464f", BL = "#0a6fe0";
const FONT = "Inter, system-ui, sans-serif";
const A = [4.2, 7.2, 10.2, 13.2], HIT = 21.6, W0 = 18.6;
const clamp = (x: number, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const sstep = (x: number) => { x = clamp(x); return x * x * x * (x * (6 * x - 15) + 10); };
const eo = (x: number) => 1 - Math.pow(1 - clamp(x), 3);

// Spring über Sekunden-Zeit
const useSp = (at: number, cfg = { damping: 14, stiffness: 120, mass: 0.8 }) => {
  const f = useCurrentFrame(); const { fps } = useVideoConfig();
  return spring({ frame: f - at * fps, fps, config: cfg });
};
const useT = () => { const f = useCurrentFrame(); return f / 30; };

const Txt: React.FC<{ size: number; color?: string; weight?: number; style?: React.CSSProperties; children: React.ReactNode }> = ({ size, color = WH, weight = 800, style, children }) => (
  <div style={{ fontFamily: FONT, fontSize: size, fontWeight: weight, color, textAlign: "center", lineHeight: 1.1, ...style }}>{children}</div>
);

// ---------- Hook + Intro ----------
const Hook: React.FC = () => {
  const t = useT();
  const slam = t < 0.17 ? 6 + (470 - 6) * Math.pow(t / 0.17, 3) : interpolate(sstep((t - 0.45) / 0.8), [0, 1], [470, 22]);
  const cx = 540, cy = interpolate(sstep((t - 0.45) / 0.8), [0, 1], [1000, 938]);
  const q = (t - 0.17) / 0.3;
  const k = q > 0 && q < 1 ? 1 + 0.4 * Math.sin(Math.PI * q) * Math.exp(-1.5 * q) : 1;
  const shake = t > 0.17 && t < 0.9 ? 26 * Math.exp(-(t - 0.17) * 9) * Math.sin((t - 0.17) * 70) : 0;
  const a1 = eo((t - 0.5) / 0.3) * (1 - sstep((t - 1.9) / 0.25)), a2 = eo((t - 0.7) / 0.3) * (1 - sstep((t - 1.9) / 0.25));
  const flash = t >= 0.17 && t < 0.3 ? 0.16 * (1 - (t - 0.17) / 0.13) : 0;
  const shards = Array.from({ length: 18 }, (_, i) => {
    const tt = t - 0.17; if (tt < 0 || tt > 0.63) return null;
    const ang = (i * 2.399 + 0.7) % (2 * Math.PI), v = 500 + (i % 6) * 100, sz = 8 + (i % 5) * 3;
    return <div key={i} style={{ position: "absolute", left: 540 + Math.cos(ang) * v * tt, top: 1000 + Math.sin(ang) * v * tt + 900 * tt * tt, width: sz, height: sz, borderRadius: sz, background: OR, opacity: 1 - tt / 0.63 }} />;
  });
  const words = ["Wir", "bauen", "sie.", "Du", "entscheidest."];
  return (
    <AbsoluteFill style={{ transform: `translate(${shake}px,${shake * 0.7}px)` }}>
      {t < 4 && <div style={{ position: "absolute", left: cx - slam, top: cy - slam, width: slam * 2, height: slam * 2, borderRadius: "50%", background: `radial-gradient(circle at 35% 30%, ${ORL}, ${OR} 48%, ${ORD})`, transform: `scale(${k},${1 / k})`, boxShadow: `0 0 90px 24px rgba(255,159,28,.3)`, opacity: t < 2.4 ? 1 : 1 - sstep((t - 2.4) / 1.4) }} />}
      {shards}
      <div style={{ position: "absolute", top: 1180, width: "100%", opacity: a1, transform: `translateY(${(1 - eo((t - 0.5) / 0.3)) * 36}px)` }}><Txt size={96}>Noch keine Website,</Txt></div>
      <div style={{ position: "absolute", top: 1290, width: "100%", opacity: a2, transform: `translateY(${(1 - eo((t - 0.7) / 0.3)) * 36}px)` }}><Txt size={96} color={OR}>die Kunden bringt?</Txt></div>
      <div style={{ position: "absolute", top: 480, width: "100%", display: "flex", flexDirection: "column", alignItems: "center", gap: 10 }}>
        {[words.slice(0, 3), words.slice(3)].map((line, li) => (
          <div key={li} style={{ display: "flex", gap: 24 }}>
            {line.map((w, wi) => { const i = li * 3 + wi; const s = eo((t - (2.1 + i * 0.12)) / 0.38); const out = 1 - sstep((t - 3.6) / 0.3); return <Txt key={w} size={84} style={{ opacity: s * out, transform: `translateY(${(1 - s) * 40}px)` }}>{w}</Txt>; })}
          </div>
        ))}
      </div>
      <AbsoluteFill style={{ background: "#fff", opacity: flash }} />
    </AbsoluteFill>
  );
};

// ---------- Stationen ----------
const Title: React.FC<{ n: number; title: string; sub: string }> = ({ n, title, sub }) => {
  const t = useT(); const s = eo((t - 0.05) / 0.3); const out = 1 - sstep((t - 2.1) / 0.3);
  return (
    <div style={{ position: "absolute", top: 250, width: "100%", opacity: s * out, transform: `translateY(${(1 - s) * 24}px)` }}>
      <div style={{ display: "flex", justifyContent: "center", alignItems: "center", gap: 24 }}>
        <div style={{ width: 76, height: 76, borderRadius: 38, background: OR, boxShadow: `0 6px 0 ${ORD}`, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: FONT, fontWeight: 800, fontSize: 46, color: "#fff" }}>{n}</div>
        <Txt size={92}>{title}</Txt>
      </div>
      <Txt size={44} color={GR} weight={500} style={{ marginTop: 18 }}>{sub}</Txt>
    </div>
  );
};
const Pop: React.FC<{ children: React.ReactNode; top: number }> = ({ children, top }) => {
  const t = useT(); const u = spring({ frame: t * 30, fps: 30, config: { damping: 11, stiffness: 140, mass: 0.7 } });
  const out = 1 - sstep((t - 2.3) / 0.4);
  return <div style={{ position: "absolute", top, left: 0, width: "100%", display: "flex", justifyContent: "center", opacity: clamp(t / 0.2) * out, transform: `scale(${clamp(0.15 + 0.85 * u, 0.05, 1.12)})` }}>{children}</div>;
};
const card: React.CSSProperties = { background: CARD, border: `3px solid ${EDGE}`, borderRadius: 48, position: "relative" };
const Bubble: React.FC<{ at: number; style: React.CSSProperties; children: React.ReactNode }> = ({ at, style, children }) => {
  const t = useT(); const s = t > at ? spring({ frame: (t - at) * 30, fps: 30, config: { damping: 9, stiffness: 160, mass: 0.6 } }) : 0;
  return <div style={{ position: "absolute", fontFamily: FONT, fontWeight: 800, fontSize: 38, lineHeight: 1.3, padding: "24px 34px", borderRadius: 36, textAlign: "center", transform: `scale(${s})`, opacity: s > 0 ? 1 : 0, ...style }}>{children}</div>;
};
const S1: React.FC = () => (
  <AbsoluteFill>
    <Title n={1} title="Erstgespräch" sub="Kostenlos. Unverbindlich." />
    <Pop top={600}><div style={{ ...card, width: 780, height: 600 }}>
      <div style={{ position: "absolute", left: 36, top: 34, display: "flex", alignItems: "center", gap: 16, fontFamily: FONT, fontWeight: 800, fontSize: 38, color: WH }}><div style={{ width: 56, height: 56, borderRadius: 28, background: OR }} />sherka.</div>
      <div style={{ position: "absolute", left: 40, right: 40, top: 130, height: 2, background: EDGE }} />
      <Bubble at={0.45} style={{ right: 44, top: 180, background: OR, color: "#201400" }}>Ich brauche eine<br />neue Website.</Bubble>
      <Bubble at={1.35} style={{ left: 44, top: 360, width: 600, background: "#2d3c44", color: WH }}>Gerne! Wir antworten<br />innert eines Werktags.</Bubble>
    </div></Pop>
  </AbsoluteFill>
);
const S2: React.FC = () => {
  const t = useT(); const done = t > 1.55; const pin = t > 0.7 ? spring({ frame: (t - 0.7) * 30, fps: 30, config: { damping: 9, stiffness: 160, mass: 0.6 } }) : 0;
  return (
    <AbsoluteFill>
      <Title n={2} title="Entwurf" sub="Du siehst ihn. Du kommentierst." />
      <Pop top={480}><div style={{ position: "relative", width: 560, height: 880 }}>
        <div style={{ position: "absolute", left: 60, top: 0, width: 436, height: 800, borderRadius: 52, background: "#32323a" }} />
        <div style={{ position: "absolute", left: 70, top: 10, width: 416, height: 780, borderRadius: 42, overflow: "hidden" }}><Img src={staticFile("bledi.png")} style={{ width: 416 }} /></div>
        <div style={{ position: "absolute", left: 330, top: 214, height: 72, padding: "0 24px", borderRadius: 36, background: done ? "#3cbe5a" : OR, color: done ? "#fff" : "#1e1400", fontFamily: FONT, fontWeight: 800, fontSize: 34, display: "flex", alignItems: "center", whiteSpace: "nowrap", transform: `scale(${pin})`, transformOrigin: "0 50%", boxShadow: `0 6px 0 ${done ? "#1f7a35" : "#8a5300"}` }}>{done ? "✓ Erledigt" : "Button grösser?"}</div>
        <div style={{ position: "absolute", top: 822, width: "100%", textAlign: "center", fontFamily: FONT, fontWeight: 700, fontSize: 40, color: GR }}>bledi-bienne.ch</div>
      </div></Pop>
    </AbsoluteFill>
  );
};
const S3: React.FC = () => {
  const t = useT(); const before = t < 1.1; const press = sstep((t - 0.85) / 0.1);
  const ck = spring({ frame: (t - 1.1) * 30, fps: 30, config: { damping: 8, stiffness: 140, mass: 0.7 } });
  return (
    <AbsoluteFill>
      <Title n={3} title="Freigabe" sub="Online geht nur, was du freigibst" />
      <Pop top={640}><div style={{ ...card, width: 780, height: 560, textAlign: "center" }}>
        {before ? (<>
          <Txt size={62} style={{ position: "absolute", top: 84, width: "100%" }}>Entwurf bereit</Txt>
          <Txt size={40} color={GR} weight={500} style={{ position: "absolute", top: 170, width: "100%" }}>Passt alles so?</Txt>
          <div style={{ position: "absolute", left: 120, right: 120, top: 240, height: 140, borderRadius: 22, background: "#1e2c34" }} />
          <div style={{ position: "absolute", left: 160, right: 160, top: 420 + press * 8, height: 90, borderRadius: 45, background: BL, boxShadow: `0 ${10 - press * 8}px 0 #064ea0`, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: FONT, fontWeight: 800, fontSize: 44, color: "#fff" }}>Freigeben</div>
        </>) : (<>
          <div style={{ position: "absolute", left: 290, top: 120, width: 200, height: 200, borderRadius: 100, background: OR, boxShadow: `0 12px 0 ${ORD}`, transform: `scale(${clamp(ck, 0, 1.12)})`, display: "flex", alignItems: "center", justifyContent: "center" }}>
            <svg width="200" height="200" viewBox="0 0 200 200"><polyline points="52,102 88,138 150,64" fill="none" stroke="#fff" strokeWidth="16" strokeLinecap="round" strokeLinejoin="round" /></svg></div>
          <Txt size={66} style={{ position: "absolute", top: 380, width: "100%", opacity: eo((t - 1.3) / 0.3) }}>Freigegeben</Txt>
          <Txt size={38} color={GR} weight={500} style={{ position: "absolute", top: 462, width: "100%", opacity: eo((t - 1.5) / 0.3) }}>Jetzt gehen wir online.</Txt>
        </>)}
      </div></Pop>
    </AbsoluteFill>
  );
};
const S4: React.FC = () => {
  const t = useT(); const pill = t > 0.6 ? spring({ frame: (t - 0.6) * 30, fps: 30, config: { damping: 9, stiffness: 160, mass: 0.6 } }) : 0; const ch = eo((t - 1.2) / 0.3);
  return (
    <AbsoluteFill>
      <Title n={4} title="Online" sub="Die Domain gehört dir." />
      <Pop top={520}><div style={{ position: "relative", width: 880, height: 780 }}>
        <div style={{ position: "absolute", left: 335, top: 20, width: 210, height: 68, borderRadius: 34, background: "#16222a", border: "3px solid #3cbe5a", display: "flex", alignItems: "center", justifyContent: "center", gap: 12, fontFamily: FONT, fontWeight: 800, fontSize: 36, color: WH, transform: `scale(${pill})` }}><div style={{ width: 20, height: 20, borderRadius: 10, background: "#3cdc64" }} />Online</div>
        <div style={{ position: "absolute", left: 78, top: 88, width: 764, height: 494, borderRadius: 24, background: "#2e2e34" }} />
        <div style={{ position: "absolute", left: 100, top: 110, width: 720, height: 450, overflow: "hidden" }}><Img src={staticFile("zahnarzt.png")} style={{ width: 720 }} /></div>
        <div style={{ position: "absolute", left: 20, top: 582, width: 840, height: 26, borderRadius: 12, background: "#c4c4cc" }} />
        <div style={{ position: "absolute", left: 200, top: 640, width: 480, height: 72, borderRadius: 36, background: "#16222a", border: `2px solid ${EDGE}`, display: "flex", alignItems: "center", justifyContent: "center", gap: 14, fontFamily: FONT, fontWeight: 800, fontSize: 36, color: WH, opacity: ch }}>deine-firma.ch <span style={{ color: OR, fontWeight: 500, fontSize: 32 }}>gehört dir</span></div>
        <div style={{ position: "absolute", top: 742, width: "100%", textAlign: "center", fontFamily: FONT, fontWeight: 700, fontSize: 40, color: GR, opacity: ch }}>bern-zahnarzt-team.ch</div>
      </div></Pop>
    </AbsoluteFill>
  );
};

// ---------- Rückblick, Wörter, Hero ----------
const Recap: React.FC = () => {
  const t = useT(); const out = 1 - sstep((t - 2.2) / 0.4); const names = ["Erstgespräch", "Entwurf", "Freigabe", "Online"];
  return (
    <AbsoluteFill style={{ opacity: out }}>
      <div style={{ position: "absolute", left: 290, top: 640, width: 14, height: 630 * sstep((t - 0.2) / 1.7), borderRadius: 7, background: OR, boxShadow: `0 0 20px ${OR}` }} />
      {names.map((n, k) => { const a = eo((t - (0.1 + k * 0.45)) / 0.35); return (
        <div key={n} style={{ position: "absolute", left: 240, top: 640 + k * 210 - 46, display: "flex", alignItems: "center", gap: 36, opacity: a, transform: `scale(${0.9 + 0.1 * a})`, transformOrigin: "0 50%" }}>
          <div style={{ width: 92, height: 92, borderRadius: 46, background: OR, boxShadow: `0 8px 0 ${ORD}`, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: FONT, fontWeight: 800, fontSize: 46, color: "#fff" }}>{k + 1}</div>
          <Txt size={84}>{n}</Txt></div>); })}
    </AbsoluteFill>
  );
};
const WordCard: React.FC<{ txt: string; hot: boolean; at: number; x: number; y: number; rot: number }> = ({ txt, hot, at, x, y, rot }) => {
  const t = useT(); const fade = 1 - sstep((t - 2.6) / 0.3); if (t < at) return null;
  const s = spring({ frame: (t - at) * 30, fps: 30, config: { damping: 7, stiffness: 90, mass: 1.1 } });
  const yy = interpolate(s, [0, 1], [-200, y]); const w = txt.length * 62 + 90;
  return <div style={{ position: "absolute", left: x - w / 2, top: yy - 75, width: w, height: 150, borderRadius: 34, background: hot ? OR : CARD, border: `3px solid ${hot ? ORD : EDGE}`, boxShadow: `0 12px 0 ${hot ? ORD : "#0b0e11"}`, color: hot ? "#201400" : WH, fontFamily: FONT, fontWeight: 800, fontSize: 96, display: "flex", alignItems: "center", justifyContent: "center", transform: `rotate(${rot * clamp(s, 0, 1)}deg)`, opacity: fade }}>{txt}</div>;
};
const Words: React.FC = () => (
  <AbsoluteFill>
    <WordCard txt="Mehr" hot={false} at={0.15} x={330} y={1165} rot={-8} />
    <WordCard txt="Kunden." hot at={0.55} x={730} y={1165} rot={5} />
    <WordCard txt="Weniger" hot={false} at={0.95} x={400} y={980} rot={4} />
    <WordCard txt="Aufwand." hot at={1.35} x={640} y={820} rot={-6} />
  </AbsoluteFill>
);
const Hero: React.FC = () => {
  const t = useT(); const ic = spring({ frame: t * 30, fps: 30, config: { damping: 8, stiffness: 150, mass: 0.7 } });
  const flash = t < 0.12 ? 0.22 * (1 - t / 0.12) : 0; const up = sstep((t - 0.1) / 0.5); const ul = sstep((t - 0.5) / 0.7);
  const cta = spring({ frame: (t - 0.8) * 30, fps: 30, config: { damping: 10, stiffness: 140, mass: 0.7 } });
  const ring = t < 0.6 ? eo(t / 0.6) : 1;
  return (
    <AbsoluteFill>
      <div style={{ position: "absolute", left: 540 - 520 * ring, top: 700 - 182 * ring, width: 1040 * ring, height: 364 * ring, borderRadius: "50%", border: `5px solid ${ORL}`, opacity: t < 0.6 ? (1 - t / 0.6) * 0.8 : 0 }} />
      <Img src={staticFile("icon-crop.png")} style={{ position: "absolute", left: 540 - 121, top: 470, height: 300, transform: `scale(${clamp(ic, 0, 1.08)})`, filter: `drop-shadow(0 0 20px rgba(255,159,28,.5))` }} />
      <div style={{ position: "absolute", top: 860, width: "100%", display: "flex", justifyContent: "center", clipPath: `inset(-20px ${100 - 100 * up}% -20px 0)` }}><Txt size={124}>sherka<span style={{ color: OR }}>.ch</span></Txt></div>
      <div style={{ position: "absolute", left: 540 - 380, top: 1010, width: 760 * ul, height: 10, borderRadius: 5, background: OR, boxShadow: `0 0 16px ${OR}`, transform: "rotate(-.5deg)" }} />
      <div style={{ position: "absolute", left: 190, top: 1265, width: 700, height: 130, borderRadius: 65, background: BL, boxShadow: "0 12px 0 #064ea0", display: "flex", alignItems: "center", justifyContent: "center", fontFamily: FONT, fontWeight: 800, fontSize: 54, color: "#fff", transform: `scale(${clamp(cta, 0, 1.08)})` }}>Erstgespräch anfragen</div>
      <Txt size={44} color={GR} weight={500} style={{ position: "absolute", top: 1430, width: "100%", opacity: eo((t - 1.3) / 0.4) }}>Kostenlos und unverbindlich</Txt>
      <Txt size={44} color={OR} style={{ position: "absolute", top: 1500, width: "100%", opacity: eo((t - 1.6) / 0.4) }}>Link in der Bio</Txt>
      <AbsoluteFill style={{ background: "#fff", opacity: flash }} />
    </AbsoluteFill>
  );
};

export const Reel: React.FC = () => {
  const s = (sec: number) => Math.round(sec * 30);
  return (
    <AbsoluteFill style={{ background: `radial-gradient(900px 1100px at 540px 1000px, #1b1710 0%, #08090c 70%)` }}>
      <Audio src={staticFile("audio.mp3")} />
      <Sequence from={0} durationInFrames={s(4.2)}><Hook /></Sequence>
      <Sequence from={s(A[0])} durationInFrames={s(3)}><S1 /></Sequence>
      <Sequence from={s(A[1])} durationInFrames={s(3)}><S2 /></Sequence>
      <Sequence from={s(A[2])} durationInFrames={s(3)}><S3 /></Sequence>
      <Sequence from={s(A[3])} durationInFrames={s(3)}><S4 /></Sequence>
      <Sequence from={s(16.2)} durationInFrames={s(2.6)}><Recap /></Sequence>
      <Sequence from={s(W0)} durationInFrames={s(3.2)}><Words /></Sequence>
      <Sequence from={s(HIT)} durationInFrames={s(2.4)}><Hero /></Sequence>
    </AbsoluteFill>
  );
};
