"""Build self-contained profile SVGs with Python 3; no dependencies."""
from pathlib import Path
from html import escape
import xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / 'img'
FONT = 'Segoe UI,Arial,Noto Sans KR,sans-serif'
def svg(w,h,title,body):
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}"><title>{escape(title)}</title>{body}</svg>\n'
projects = [
 ('speech-to-text','01 / VOICE INTELLIGENCE','녹음을 읽을 수 있는 기록으로','한국어 전사 · 화자 구분 · 타임스탬프','Python / Whisper / Local AI','#58a6ff','<path d="M8 22v12m8-22v32m8-38v44m8-32v20m8-26v32"/>'),
 ('socratic-claude','02 / REASONING AGENTS','답하기 전에, 전제부터 질문합니다','숨은 전제를 검토하는 Claude Code 플러그인','Python / Claude Code / Agents','#bc9cff','<path d="M6 7h34v26H23L12 43V33H6Z M19 17c0-8 12-8 12 0 0 5-6 4-6 9m0 4v1"/>'),
 ('photo-blog-agent','03 / CREATIVE AUTOMATION','사진에서 시작하는 블로그 워크플로','프롬프트 · 스크립트 · 스키마로 잇는 자동화','JavaScript / Claude Code / Workflow','#42d6b0','<rect x="4" y="10" width="40" height="30" rx="5"/><circle cx="24" cy="25" r="8"/><path d="M13 10l4-6h14l4 6"/>'),
 ('md-viewer','04 / DEVELOPER TOOLS','문서를 여는 순간, 작업이 시작됩니다','가볍게 열고 읽고 편집하는 Markdown 도구','TypeScript / WebView2 / Windows','#ffb86b','<path d="M11 3h22l9 9v35H11Z M33 3v12h9 M17 25v12m0-12 6 7 6-7v12m5-10v10m-3-3 3 3 3-3"/>'),
]
for name,category,headline,desc,stack,color,icon in projects:
 body=f'''<defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#142338"/><stop offset="1" stop-color="#0d1117"/></linearGradient></defs>
 <rect x="1" y="1" width="558" height="238" rx="18" fill="url(#bg)" stroke="#303d50"/>
 <path d="M22 1h95" stroke="{color}" stroke-width="3"/>
 <text x="26" y="35" fill="{color}" font-family="{FONT}" font-size="12" letter-spacing="2">{category}</text>
 <g transform="translate(478 24)" fill="none" stroke="{color}" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round">{icon}</g>
 <text x="26" y="82" fill="#f0f6fc" font-family="{FONT}" font-size="29" font-weight="700">{name}</text>
 <text x="26" y="119" fill="#e6edf3" font-family="{FONT}" font-size="21" font-weight="600">{headline}</text>
 <text x="26" y="150" fill="#a9b9cc" font-family="{FONT}" font-size="17">{desc}</text>
 <path d="M26 177h508" stroke="#26364a"/>
 <text x="26" y="210" fill="{color}" font-family="{FONT}" font-size="14">{stack}</text>
 <path d="M505 204h20m-6-6 6 6-6 6" stroke="{color}" stroke-width="2" fill="none"/>'''
 (IMG/f'project-{name}.svg').write_text(svg(560,240,name+' — '+headline,body))
techs=[('python','Python','#ffd45a'),('typescript','TypeScript','#58a6ff'),('javascript','JavaScript','#f7df1e'),('react','React','#61dafb'),('nextdotjs','Next.js','#f0f6fc'),('nodedotjs','Node.js','#81c668'),('docker','Docker','#58a6ff'),('git','Git','#f78166'),('github','GitHub','#f0f6fc')]
for index,group in enumerate([techs[:5],techs[5:]],1):
 body=''
 for i,(slug,label,color) in enumerate(group):
  paths=''.join(ET.tostring(el,encoding='unicode') for el in ET.parse(IMG/'tech'/f'{slug}.svg').getroot() if el.tag.endswith('path'))
  x=i*104
  body+=f'<rect x="{x+3}" y="3" width="96" height="102" rx="16" fill="#111c2c" stroke="#29384c"/><g transform="translate({x+31} 19) scale(1.7)" fill="{color}">{paths}</g><text x="{x+51}" y="85" text-anchor="middle" font-family="{FONT}" font-size="13" fill="#d8e4f0">{label}</text>'
 (IMG/f'tech-stack-{index}.svg').write_text(svg(len(group)*104,108,' · '.join(t[1] for t in group),body))
body='''<style>@keyframes pulse{0%,100%{opacity:.35}50%{opacity:1}}@keyframes orbit{to{transform:rotate(360deg)}}.orb{transform-origin:450px 32px;animation:orbit 12s linear infinite}.light{animation:pulse 4s ease-in-out infinite}@media(prefers-reduced-motion:reduce){.orb,.light{animation:none}}</style>
<path d="M0 32h370m160 0h370" stroke="#263d59"/><path d="M310 32h60m160 0h60" stroke="#58a6ff" class="light"/>
<ellipse cx="450" cy="32" rx="52" ry="17" fill="none" stroke="#58a6ff" opacity=".65"/>
<ellipse cx="450" cy="32" rx="52" ry="17" transform="rotate(-25 450 32)" fill="none" stroke="#58a6ff" opacity=".4"/>
<circle cx="450" cy="32" r="6" fill="#79c0ff" class="light"/><g class="orb"><circle cx="479" cy="32" r="3" fill="#bc9cff"/></g>'''
(IMG/'electron-divider.svg').write_text(svg(900,64,'Electron orbit',body))
print('Built 4 project cards, 2 technology strips, and animated divider.')
