
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="LearnIQ", layout="wide", page_icon="🧠")

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@300;400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; }

.stApp { background-color: #060d1f; font-family: 'DM Sans', sans-serif; color: #e2eaff; }
#MainMenu, footer, header { visibility: hidden; }


.block-container {
    padding: 1.5rem 1.5rem !important;
    max-width: 1400px;
}
@media (min-width: 768px) {
    .block-container { padding: 2rem 3rem !important; }
}


.top-header {
    display: flex;
    flex-direction: column;
    gap: 12px;
    padding: 16px 18px;
    background: linear-gradient(135deg, #0a1428, #0d1e3d);
    border: 1px solid #1a2e55;
    border-radius: 16px;
    margin-bottom: 20px;
}
@media (min-width: 600px) {
    .top-header {
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        padding: 18px 32px;
        border-radius: 20px;
        margin-bottom: 28px;
    }
}
.brand-name {
    font-family: 'Syne', sans-serif;
    font-size: 22px;
    font-weight: 800;
    background: linear-gradient(90deg, #38bdf8, #06b6d4);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
@media (min-width: 600px) { .brand-name { font-size: 26px; } }
.brand-sub { font-size: 11px; color: #4a6080; letter-spacing: 1.2px; text-transform: uppercase; }
.badges { display: flex; gap: 8px; flex-wrap: wrap; }
.badge { padding: 5px 12px; border-radius: 20px; font-size: 11px; font-weight: 500; }
.badge-blue { background: rgba(56,189,248,0.12); color: #38bdf8; border: 1px solid rgba(56,189,248,0.25); }
.badge-cyan { background: rgba(6,182,212,0.12);  color: #06b6d4; border: 1px solid rgba(6,182,212,0.25); }


.kpi-strip {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    margin-bottom: 20px;
}
@media (min-width: 600px) {
    .kpi-strip { grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 28px; }
}
.kpi-card {
    background: #0a1428; border: 1px solid #1a2e55; border-radius: 14px;
    padding: 14px 16px; position: relative; overflow: hidden;
}
@media (min-width: 600px) { .kpi-card { border-radius: 16px; padding: 20px 22px; } }
.kpi-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px; }
.kpi-card.blue::before   { background: linear-gradient(90deg, #38bdf8, transparent); }
.kpi-card.cyan::before   { background: linear-gradient(90deg, #06b6d4, transparent); }
.kpi-card.indigo::before { background: linear-gradient(90deg, #818cf8, transparent); }
.kpi-card.sky::before    { background: linear-gradient(90deg, #7dd3fc, transparent); }
.kpi-label { font-size: 10px; text-transform: uppercase; letter-spacing: 1.2px; color: #4a6080; margin-bottom: 6px; }
@media (min-width: 600px) { .kpi-label { font-size: 11px; letter-spacing: 1.5px; margin-bottom: 10px; } }
.kpi-value { font-family: 'Syne', sans-serif; font-size: 22px; font-weight: 700; color: #e2eaff; }
@media (min-width: 600px) { .kpi-value { font-size: 28px; } }
.kpi-value span { font-size: 12px; color: #4a6080; font-weight: 400; }
.kpi-sub { font-size: 11px; color: #2a4060; margin-top: 4px; }


.panel { background: #0a1428; border: 1px solid #1a2e55; border-radius: 16px; padding: 18px; }
@media (min-width: 600px) { .panel { border-radius: 20px; padding: 28px; } }
.panel-title {
    font-family: 'Syne', sans-serif; font-size: 14px; font-weight: 700;
    color: #c7d9f5; margin-bottom: 16px; padding-bottom: 10px; border-bottom: 1px solid #1a2e55;
}
@media (min-width: 600px) { .panel-title { font-size: 16px; margin-bottom: 22px; } }


.stSlider label { color: #7a9cc0 !important; font-size: 12px !important; }
@media (min-width: 600px) { .stSlider label { font-size: 13px !important; } }


.stButton > button {
    width: 100%; height: 48px; border-radius: 12px;
    background: linear-gradient(135deg, #0ea5e9, #06b6d4) !important;
    color: #ffffff !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 14px !important; font-weight: 700 !important; border: none !important;
    box-shadow: 0 0 24px rgba(14,165,233,0.3) !important;
    touch-action: manipulation;
}
@media (min-width: 600px) { .stButton > button { height: 52px; border-radius: 14px; font-size: 15px !important; } }


.result-box {
    background: #071020; border: 1px solid #1a3a5c;
    border-radius: 14px; padding: 16px; margin-bottom: 14px;
}
.result-title {
    font-family: 'Syne', sans-serif; font-size: 11px; text-transform: uppercase;
    letter-spacing: 2px; color: #38bdf8; margin-bottom: 10px;
}
.sug-item {
    padding: 9px 12px; background: rgba(56,189,248,0.05);
    border: 1px solid rgba(56,189,248,0.12); border-radius: 10px;
    margin-bottom: 8px; font-size: 13px; color: #a8c4e0; line-height: 1.5;
}
.excellent {
    text-align: center; padding: 20px;
    background: linear-gradient(135deg, rgba(56,189,248,0.08), rgba(6,182,212,0.08));
    border: 1px solid rgba(56,189,248,0.2); border-radius: 14px;
    font-family: 'Syne', sans-serif; font-size: 17px; color: #38bdf8;
}


.score-wrap {
    background: #060d1f; border: 1px solid #1a2e55;
    border-radius: 14px; padding: 16px; margin-top: 14px; text-align: center;
}
.score-label { font-size: 10px; text-transform: uppercase; letter-spacing: 2px; color: #4a6080; margin-bottom: 6px; }
.score-number {
    font-family: 'Syne', sans-serif; font-size: 42px; font-weight: 800;
    background: linear-gradient(90deg, #38bdf8, #06b6d4);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.score-bar-outer { width: 100%; height: 7px; background: #1a2e55; border-radius: 99px; margin-top: 10px; overflow: hidden; }
.score-bar-inner { height: 100%; border-radius: 99px; background: linear-gradient(90deg, #38bdf8, #06b6d4); }


.chart-title {
    font-family: 'Syne', sans-serif; font-size: 16px; font-weight: 700;
    color: #c7d9f5; margin-bottom: 6px; padding-bottom: 12px; border-bottom: 1px solid #1a2e55;
}
@media (min-width: 600px) { .chart-title { font-size: 18px; } }
.chart-desc { font-size: 12px; color: #4a6080; margin-bottom: 16px; }
.chart-card {
    background: #0a1428; border: 1px solid #1a2e55; border-radius: 14px; padding: 16px; margin-bottom: 16px;
}
.chart-card-title { font-family: 'Syne', sans-serif; font-size: 13px; font-weight: 700; color: #c7d9f5; margin-bottom: 3px; }
.chart-card-sub   { font-size: 11px; color: #4a6080; margin-bottom: 12px; line-height: 1.5; }


.empty-state {
    height: 260px; display: flex; flex-direction: column; align-items: center;
    justify-content: center; border: 1px dashed #1a2e55; border-radius: 16px; gap: 10px;
    padding: 20px; text-align: center;
}
.empty-title { font-family: 'Syne', sans-serif; font-size: 16px; color: #2a4060; }
.empty-sub   { font-size: 12px; color: #2a4060; max-width: 240px; }

.footer-bar {
    margin-top: 28px; padding: 14px 18px; background: #0a1428;
    border: 1px solid #1a2e55; border-radius: 14px;
    display: flex; flex-direction: column; gap: 6px;
    font-size: 12px; color: #2a4060; text-align: center;
}
@media (min-width: 768px) {
    .footer-bar {
        flex-direction: row; align-items: center; justify-content: space-between;
        padding: 18px 28px; font-size: 13px; text-align: left; gap: 0;
    }
}


.stDataFrame { border-radius: 10px !important; overflow: hidden !important; }


@media (max-width: 640px) {
    div[data-testid="column"] { min-width: 100% !important; }
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)
df = pd.read_csv("student_productivity_dataset.csv")

def recommend(d):
    s = []
    if d['exam_score'] < 50:
        s.append(("📘", "Revise basic concepts - exam score needs improvement"))
    elif d['exam_score'] < 70:
        s.append(("📖", "Aim for deeper understanding - exam score is average"))
    if d['study_hours'] < 2:
        s.append(("⏰", "Increase daily study time to at least 3-4 hours"))
    elif d['study_hours'] < 4:
        s.append(("📅", "Try to add 1 more focused hour of study per day"))
    if d['screen_time'] > 6:
        s.append(("📵", "Reduce screen time - it is impacting focus and sleep"))
    elif d['screen_time'] > 4:
        s.append(("📱", "Moderate screen time for better concentration"))
    if d['stress_level'] > 7:
        s.append(("🧘", "Critical stress - try meditation or breathing exercises"))
    elif d['stress_level'] > 5:
        s.append(("😌", "Manage stress through regular breaks and exercise"))
    if d['attendance'] < 60:
        s.append(("🏫", "Attendance very low - prioritize attending classes"))
    elif d['attendance'] < 75:
        s.append(("📆", "Attendance below 75% - try not to miss lectures"))
    if d['assignment_score'] < 50:
        s.append(("📝", "Focus on completing and improving assignments"))
    if d['sleep_hours'] < 6:
        s.append(("😴", "Need more sleep - aim for 7-8 hours for better retention"))
    elif d['sleep_hours'] > 9:
        s.append(("⏰", "Oversleeping affects productivity - balance rest and action"))
    return s

def perf_tier(score):
    if score >= 140: return "Elite",      "#38bdf8"
    if score >= 110: return "Strong",     "#06b6d4"
    if score >= 80:  return "Developing", "#818cf8"
    return "Needs Work", "#f87171"

plt.rcParams.update({
    'figure.facecolor': '#0a1428', 'axes.facecolor': '#0a1428',
    'axes.edgecolor': '#1a2e55',   'axes.labelcolor': '#4a6080',
    'xtick.color': '#2a4060',      'ytick.color': '#2a4060',
    'text.color': '#7a9cc0',       'grid.color': '#1a2e55',
    'grid.linestyle': '--',        'grid.alpha': 0.5,
    'font.family': 'sans-serif',
})

BLUE   = "#38bdf8"
CYAN   = "#06b6d4"
INDIGO = "#818cf8"
RED    = "#f87171"

st.markdown("""
<div class="top-header">
  <div style="display:flex;align-items:center;gap:12px;">
    <div style="width:44px;height:44px;min-width:44px;background:linear-gradient(135deg,#0ea5e9,#06b6d4);
         border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:20px;">🧠</div>
    <div>
      <div class="brand-name">LearnIQ</div>
      <div class="brand-sub">AI Personalized Learning Engine</div>
    </div>
  </div>
  <div class="badges" style="margin-top:4px;">
    <div class="badge badge-blue">&#9679; Live</div>
    <div class="badge badge-cyan">v2.0 Ocean</div>
  </div>
</div>
""", unsafe_allow_html=True)

avg_study  = round(df['study_hours'].mean(), 1)
avg_stress = round(df['stress_level'].mean(), 1)
avg_attend = round(df['attendance'].mean(), 1)
avg_exam   = round(df['exam_score'].mean(), 1)

st.markdown(f"""
<div class="kpi-strip">
  <div class="kpi-card blue">
    <div class="kpi-label">Avg Study Time</div>
    <div class="kpi-value">{avg_study}<span> hrs</span></div>
    <div class="kpi-sub">All students</div>
  </div>
  <div class="kpi-card indigo">
    <div class="kpi-label">Avg Stress</div>
    <div class="kpi-value">{avg_stress}<span> /10</span></div>
    <div class="kpi-sub">Lower is better</div>
  </div>
  <div class="kpi-card cyan">
    <div class="kpi-label">Avg Attendance</div>
    <div class="kpi-value">{avg_attend}<span> %</span></div>
    <div class="kpi-sub">Class presence</div>
  </div>
  <div class="kpi-card sky">
    <div class="kpi-label">Avg Exam Score</div>
    <div class="kpi-value">{avg_exam}<span> /100</span></div>
    <div class="kpi-sub">Cohort benchmark</div>
  </div>
</div>
""", unsafe_allow_html=True)

left, right = st.columns([1, 1.5], gap="medium")

with left:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">🎯 Student Profile Input</div>', unsafe_allow_html=True)

    study      = st.slider("📘 Study Hours",       0, 10,  4)
    screen     = st.slider("📱 Screen Time (hrs)", 0, 10,  4)
    sleep      = st.slider("😴 Sleep Hours",       0, 10,  7)
    attendance = st.slider("🏫 Attendance %",      0, 100, 75)
    stress     = st.slider("😣 Stress Level",      0, 10,  5)
    assignment = st.slider("📝 Assignment Score",  0, 100, 70)
    exam       = st.slider("📊 Exam Score",        0, 100, 65)

    st.markdown("<br>", unsafe_allow_html=True)
    btn = st.button("🚀 Analyse and Recommend")
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    if btn:
        user_data = {
            'study_hours': study, 'sleep_hours': sleep, 'screen_time': screen,
            'stress_level': stress, 'attendance': attendance,
            'assignment_score': assignment, 'exam_score': exam
        }
        sugs = recommend(user_data)

        if not sugs:
            st.markdown("""
            <div class="excellent">
                🚀 Outstanding Performance!<br>
                <span style="font-size:13px;color:#4a6080;">All metrics in optimal range. Keep it up!</span>
            </div>""", unsafe_allow_html=True)
        else:
            items_html = "".join(
                f'<div class="sug-item">{icon} &nbsp; {text}</div>' for icon, text in sugs
            )
            st.markdown(f"""
            <div class="result-box">
                <div class="result-title">💡 Personalised Recommendations</div>
                {items_html}
            </div>""", unsafe_allow_html=True)

        score = int((study*10 + attendance*0.4 + assignment*0.4 + exam*0.4 + sleep*3)
                    - (screen*6 + stress*5))
        score = max(0, min(200, score))
        tier, tier_color = perf_tier(score)
        bar_pct = score // 2
        st.markdown(f"""
        <div class="score-wrap">
            <div class="score-label">Overall Performance Score</div>
            <div class="score-number">{score}</div>
            <div style="font-size:13px;color:{tier_color};margin-top:4px;font-weight:600;">{tier}</div>
            <div class="score-bar-outer">
                <div class="score-bar-inner" style="width:{bar_pct}%"></div>
            </div>
            <div style="display:flex;justify-content:space-between;font-size:11px;color:#2a4060;margin-top:6px;">
                <span>0</span><span>100</span><span>200</span>
            </div>
        </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="panel-title">📋 Submitted Data</div>', unsafe_allow_html=True)
        cols = ['Study','Sleep','Screen','Stress','Attend%','Assign','Exam']
        vals = [study, sleep, screen, stress, attendance, assignment, exam]
        st.dataframe(pd.DataFrame([vals], columns=cols), use_container_width=True, hide_index=True)
    else:
        st.markdown("""
        <div class="empty-state">
            <div style="font-size:44px;">🎓</div>
            <div class="empty-title">Awaiting your inputs</div>
            <div class="empty-sub">Fill in the sliders on the left and tap Analyse to get your AI recommendations.</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="chart-title">📊 Cohort Analytics Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="chart-desc">Six simple charts showing how students in your dataset are performing.</div>', unsafe_allow_html=True)

students = [f"S{sid}" for sid in df['student_id']]
FIG_W, FIG_H = 4, 3

# Row 1
col1, col2, col3 = st.columns(3, gap="small")

with col1:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-card-title">📘 Study Hours per Student</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-card-sub">Taller bar = more study. Blue line is class average.</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    colors = [BLUE if v >= avg_study else "#0d2a45" for v in df['study_hours']]
    ax.bar(students, df['study_hours'], color=colors, width=0.5, zorder=2)
    ax.axhline(avg_study, color=BLUE, linewidth=1.5, linestyle='--', label=f"Avg {avg_study}h")
    for i, v in enumerate(df['study_hours']):
        ax.text(i, v+0.15, str(v), ha='center', fontsize=9, color='#c7d9f5')
    ax.set_ylabel("Hours", fontsize=9); ax.set_ylim(0, 12)
    ax.legend(fontsize=8, facecolor='#0a1428', edgecolor='#1a2e55', labelcolor='#7a9cc0')
    ax.grid(axis='y', zorder=1); fig.tight_layout(); st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-card-title">📊 Exam Score per Student</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-card-sub">Cyan = passed (50+). Red = failed. Dashed line is pass mark.</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    colors = [CYAN if v >= 50 else RED for v in df['exam_score']]
    bars = ax.barh(students, df['exam_score'], color=colors, height=0.5, zorder=2)
    ax.axvline(50, color=RED, linewidth=1.5, linestyle='--', label="Pass (50)")
    for bar, v in zip(bars, df['exam_score']):
        ax.text(v+1, bar.get_y()+bar.get_height()/2, str(v), va='center', fontsize=9, color='#c7d9f5')
    ax.set_xlabel("Score /100", fontsize=9); ax.set_xlim(0, 115)
    ax.legend(fontsize=8, facecolor='#0a1428', edgecolor='#1a2e55', labelcolor='#7a9cc0')
    ax.grid(axis='x', zorder=1); fig.tight_layout(); st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-card-title">🏫 Attendance Categories</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-card-sub">Pie shows Good / Average / Poor attendance split.</div>', unsafe_allow_html=True)
    good  = int((df['attendance'] >= 75).sum())
    avg_a = int(((df['attendance'] >= 60) & (df['attendance'] < 75)).sum())
    poor  = int((df['attendance'] < 60).sum())
    sizes = [max(s, 0.001) for s in [good, avg_a, poor]]
    labels = [f"Good\n(>=75%)\n{good}", f"Avg\n(60-74%)\n{avg_a}", f"Poor\n(<60%)\n{poor}"]
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.pie(sizes, labels=labels, colors=[CYAN, BLUE, RED], startangle=90,
           textprops={'fontsize': 8, 'color': '#c7d9f5'},
           wedgeprops={'linewidth': 1.5, 'edgecolor': '#060d1f'})
    fig.tight_layout(); st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

# Row 2
col4, col5, col6 = st.columns(3, gap="small")

with col4:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-card-title">😣 Stress Level per Student</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-card-sub">Red bars = high stress (above 7). Purple = manageable.</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    colors = [RED if v > 7 else INDIGO for v in df['stress_level']]
    ax.bar(students, df['stress_level'], color=colors, width=0.5, zorder=2)
    ax.axhline(7, color=RED, linewidth=1.5, linestyle='--', label="High stress (7)")
    for i, v in enumerate(df['stress_level']):
        ax.text(i, v+0.15, str(v), ha='center', fontsize=9, color='#c7d9f5')
    ax.set_ylabel("Stress (0-10)", fontsize=9); ax.set_ylim(0, 12)
    ax.legend(fontsize=8, facecolor='#0a1428', edgecolor='#1a2e55', labelcolor='#7a9cc0')
    ax.grid(axis='y', zorder=1); fig.tight_layout(); st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

with col5:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-card-title">📝 Assignment vs Exam Score</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-card-sub">Blue = assignment, cyan = exam. Compare both side by side.</div>', unsafe_allow_html=True)
    x = np.arange(len(students))
    w = 0.35
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.bar(x - w/2, df['assignment_score'], w, color=BLUE,  label='Assignment', zorder=2, alpha=0.9)
    ax.bar(x + w/2, df['exam_score'],       w, color=CYAN,  label='Exam',       zorder=2, alpha=0.9)
    ax.set_xticks(x); ax.set_xticklabels(students, fontsize=9)
    ax.set_ylabel("Score /100", fontsize=9); ax.set_ylim(0, 115)
    ax.legend(fontsize=8, facecolor='#0a1428', edgecolor='#1a2e55', labelcolor='#7a9cc0')
    ax.grid(axis='y', zorder=1); fig.tight_layout(); st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

with col6:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-card-title">⚡ Productivity Score</div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-card-sub">Overall productivity. Cyan bars are above average.</div>', unsafe_allow_html=True)
    avg_prod = df['productivity_score'].mean()
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    colors = [CYAN if v >= avg_prod else "#0d2a45" for v in df['productivity_score']]
    ax.bar(students, df['productivity_score'], color=colors, width=0.5, zorder=2)
    ax.axhline(avg_prod, color=CYAN, linewidth=1.5, linestyle='--', label=f"Avg {avg_prod:.0f}")
    for i, v in enumerate(df['productivity_score']):
        ax.text(i, v+0.5, str(v), ha='center', fontsize=9, color='#c7d9f5')
    ax.set_ylabel("Score", fontsize=9); ax.set_ylim(0, 110)
    ax.legend(fontsize=8, facecolor='#0a1428', edgecolor='#1a2e55', labelcolor='#7a9cc0')
    ax.grid(axis='y', zorder=1); fig.tight_layout(); st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer-bar">
  <span>🧠 <strong style="color:#38bdf8;">LearnIQ</strong> &mdash; AI Personalized Learning Engine</span>
  <span>Consistent study + balanced lifestyle = outstanding results 🚀</span>
  <span>Built with Streamlit</span>
</div>
""", unsafe_allow_html=True)