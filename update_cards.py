
import os

file_path = r'c:\git\bezalel_arch_candidate\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the start and end markers for the section we want to replace
start_marker = '<div class="grid grid-cols-1 gap-y-24">'
# We will replace everything from start_marker until the end of the last project, 
# just before the script tag.
# Actually, let's just construct the entire new content for the div and the script.
# The script is also inside the div in the previous version? No, looking at line 930 in previous view, the script was inside.
# Let's replace the whole inner content of the grid div.

new_content = """<div class="grid grid-cols-1 gap-y-12">

                <!-- Project 1: TAMA 35 -->
                <article class="group relative flex flex-col md:flex-row gap-8 items-start">
                    <div class="w-full md:w-1/3 aspect-[16/9] bg-gray-100 overflow-hidden border border-gray-100 relative shrink-0">
                        <img src="assets/images/tama35_map_full.png"
                            class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700"
                            alt="TAMA 35">
                    </div>
                    <div class="w-full md:w-2/3">
                        <span class="text-[10px] font-bold uppercase tracking-widest text-gray-500 block mb-2">פרויקט
                            דגל לאומי | מינהל התכנון</span>
                        <h3 class="text-2xl font-black mb-3 group-hover:underline decoration-2 underline-offset-4">תמ"א
                            35: מעקב ובקרה</h3>
                        
                        <div class="relative overflow-hidden transition-all duration-500 max-h-20" id="desc-tama35">
                            <p class="text-gray-600 font-light leading-relaxed mb-4 text-sm">
                                התמ"א אושרה בשנת 2008 ומאז מהווה את "מערכת ההפעלה" של התכנון.
                                <br><br>
                                הפרויקט כולל היוועצות מבוססת נתונים ופיתוח תפיסת מעקב ובקרה המותאמת לעידן הדיגיטלי, תוך שימוש בכלים מתקדמים לניתוח והצגת המידע.
                            </p>
                        </div>
                        <button onclick="toggleDesc('tama35')" class="text-xs font-bold text-gray-400 hover:text-black mb-4 flex items-center gap-1 focus:outline-none">
                            <span id="btn-text-tama35">המשך...</span>
                            <svg class="w-3 h-3 transform rotate-0 transition-transform" id="icon-tama35" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </button>

                        <a href="https://mavat.iplan.gov.il/d434acda-7e9c-4914-a626-ce53d83c3c68" target="_blank"
                            class="inline-flex items-center gap-2 text-xs font-black bg-black text-white px-4 py-2 hover:bg-gray-800 transition-colors">
                            <span>צפה במסמכי התוכנית</span>
                            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                        </a>
                    </div>
                </article>

                <!-- Project 2: Public Participation -->
                <article class="group relative flex flex-col md:flex-row gap-8 items-start">
                    <div class="w-full md:w-1/3 aspect-[16/9] bg-gray-100 overflow-hidden border border-gray-100 relative shrink-0">
                        <img src="assets/images/physital_bot.png"
                            class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700"
                            alt="Public Participation">
                    </div>
                    <div class="w-full md:w-2/3">
                        <span class="text-[10px] font-bold uppercase tracking-widest text-gray-500 block mb-2">אגף
                            אסטרטגיה | מינהל התכנון</span>
                        <h3 class="text-2xl font-black mb-3 group-hover:underline decoration-2 underline-offset-4">שיתוף
                            ציבור והנגשת מידע</h3>
                        
                        <div class="relative overflow-hidden transition-all duration-500 max-h-20" id="desc-participation">
                            <p class="text-gray-600 font-light leading-relaxed mb-4 text-sm">
                                אפיון שיתוף ציבור בעידן הדיגיטלי, בניית מדריך ותהליכים.
                                <br><br>
                                המהלך כלל פיתוח ארגז כלים דיגיטלי (כולל בוט AI) להנגשת תהליכי תכנון לציבור הרחב, במטרה להגביר את השקיפות והמעורבות האזרחית.
                            </p>
                        </div>
                        <button onclick="toggleDesc('participation')" class="text-xs font-bold text-gray-400 hover:text-black mb-4 flex items-center gap-1 focus:outline-none">
                            <span id="btn-text-participation">המשך...</span>
                            <svg class="w-3 h-3 transform rotate-0 transition-transform" id="icon-participation" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </button>

                        <div class="flex gap-4">
                            <a href="https://participatory-assist.physital.studio/" target="_blank"
                                class="inline-flex items-center gap-2 text-xs font-black bg-black text-white px-4 py-2 hover:bg-gray-800 transition-colors">
                                <span>פתח כלי דיגיטלי</span>
                                <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                            </a>
                            <a href="https://docs.google.com/document/d/1CHihdJ0MYY2Q4xYaGrJNA24AdG-xaoQ7/edit?usp=drive_link"
                                target="_blank" class="inline-flex items-center gap-2 text-xs font-black bg-black text-white px-4 py-2 hover:bg-gray-800 transition-colors">
                                <span>מדריך שיתוף</span>
                                <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                            </a>
                        </div>
                    </div>
                </article>

                <!-- Project 3: Iplantwin -->
                <article class="group relative flex flex-col md:flex-row gap-8 items-start">
                    <div class="w-full md:w-1/3 aspect-[16/9] bg-gray-100 overflow-hidden border border-gray-100 relative shrink-0">
                        <img src="assets/images/tama35_dashboard.jpg"
                            class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700"
                            alt="Iplantwin">
                    </div>
                    <div class="w-full md:w-2/3">
                        <span class="text-[10px] font-bold uppercase tracking-widest text-gray-500 block mb-2">הדור הבא
                            | תכנון מרחבי</span>
                        <h3 class="text-2xl font-black mb-3 group-hover:underline decoration-2 underline-offset-4">
                            Iplantwin: התאום הדיגיטלי</h3>
                        
                        <div class="relative overflow-hidden transition-all duration-500 max-h-20" id="desc-twin">
                            <p class="text-gray-600 font-light leading-relaxed mb-4 text-sm">
                                אפיון "התאום הדיגיטלי" עבור מערכת התכנון הלאומית.
                                <br><br>
                                הובלת צוותי עבודה לפיתוח תשתית שתאפשר סימולציה וקבלת החלטות מבוססת נתונים בזמן אמת, כחלק מחזון העתיד של מינהל התכנון.
                            </p>
                        </div>
                        <button onclick="toggleDesc('twin')" class="text-xs font-bold text-gray-400 hover:text-black mb-4 flex items-center gap-1 focus:outline-none">
                            <span id="btn-text-twin">המשך...</span>
                            <svg class="w-3 h-3 transform rotate-0 transition-transform" id="icon-twin" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </button>
                        
                        <span class="text-xs font-bold text-gray-400 cursor-not-allowed border border-gray-200 px-3 py-1">בפיתוח</span>
                    </div>
                </article>

                <!-- Project 4: Digital Preservation TLV -->
                <article class="group relative flex flex-col md:flex-row gap-8 items-start">
                    <div class="w-full md:w-1/3 aspect-[16/9] bg-gray-100 overflow-hidden border border-gray-100 relative shrink-0">
                        <img src="assets/images/digital_preservation_tlv.png"
                            class="w-full h-full object-contain p-4 grayscale group-hover:grayscale-0 transition-all duration-700"
                            alt="Digital Preservation">
                    </div>
                    <div class="w-full md:w-2/3">
                        <span class="text-[10px] font-bold uppercase tracking-widest text-gray-500 block mb-2">עיריית תל
                            אביב-יפו</span>
                        <h3 class="text-2xl font-black mb-3 group-hover:underline decoration-2 underline-offset-4">
                            תוכנית שימור דיגיטלית</h3>
                        
                        <div class="relative overflow-hidden transition-all duration-500 max-h-20" id="desc-tlv">
                            <p class="text-gray-600 font-light leading-relaxed mb-4 text-sm">
                                פיתוח כלי לבחינת מבנים לתוכנית השימור הברוטליסטית.
                                <br><br>
                                הכלי מאפשר ניתוח זכויות בנייה והבנת ההשפעה המרחבית של אישור מבנים לשימור, תוך שימוש במודל עירוני תלת-ממדי.
                            </p>
                        </div>
                        <button onclick="toggleDesc('tlv')" class="text-xs font-bold text-gray-400 hover:text-black mb-4 flex items-center gap-1 focus:outline-none">
                            <span id="btn-text-tlv">המשך...</span>
                            <svg class="w-3 h-3 transform rotate-0 transition-transform" id="icon-tlv" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </button>

                        <a href="https://digital-conservation-tlv.physital.studio/" target="_blank"
                            class="inline-flex items-center gap-2 text-xs font-black bg-black text-white px-4 py-2 hover:bg-gray-800 transition-colors">
                            <span>מערכת השימור</span>
                            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                        </a>
                    </div>
                </article>

                <!-- Project 5: New Regionalism -->
                <article class="group relative flex flex-col md:flex-row gap-8 items-start">
                    <div class="w-full md:w-1/3 aspect-[16/9] bg-gray-100 overflow-hidden border border-gray-100 relative shrink-0">
                        <img src="assets/images/regionalism_preview.png"
                            class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700"
                            alt="Regionalism">
                    </div>
                    <div class="w-full md:w-2/3">
                        <span class="text-[10px] font-bold uppercase tracking-widest text-gray-500 block mb-2">המכון
                            למחשבה ישראלית</span>
                        <h3 class="text-2xl font-black mb-3 group-hover:underline decoration-2 underline-offset-4">לקראת
                            אזוריות חדשה</h3>
                        
                        <div class="relative overflow-hidden transition-all duration-500 max-h-20" id="desc-geo">
                            <p class="text-gray-600 font-light leading-relaxed mb-4 text-sm">
                                מחקר ופיתוח כלים (GeoData) לבחינת תבניות ייצוג של אזוריות.
                                <br><br>
                                המחקר בוחן כיצד גבולות, תשתיות וזהויות משפיעים על החברה החרדית והערבית, ומציע מודל אזורי חדש וגמיש יותר.
                            </p>
                        </div>
                        <button onclick="toggleDesc('geo')" class="text-xs font-bold text-gray-400 hover:text-black mb-4 flex items-center gap-1 focus:outline-none">
                            <span id="btn-text-geo">המשך...</span>
                            <svg class="w-3 h-3 transform rotate-0 transition-transform" id="icon-geo" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </button>

                        <a href="https://geodata.physital.studio/" target="_blank"
                            class="inline-flex items-center gap-2 text-xs font-black bg-black text-white px-4 py-2 hover:bg-gray-800 transition-colors">
                            <span>פתח כלי מחקר</span>
                            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                        </a>
                    </div>
                </article>

                <!-- Project 6: Votes120 -->
                <article class="group relative flex flex-col md:flex-row gap-8 items-start">
                    <div class="w-full md:w-1/3 aspect-[16/9] bg-gray-100 overflow-hidden border border-gray-100 relative shrink-0">
                        <img src="assets/images/vote120_preview.png"
                            class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700"
                            alt="Votes120">
                    </div>
                    <div class="w-full md:w-2/3">
                        <span class="text-[10px] font-bold uppercase tracking-widest text-gray-500 block mb-2">המכון
                            למחשבה ישראלית</span>
                        <h3 class="text-2xl font-black mb-3 group-hover:underline decoration-2 underline-offset-4">
                            בחירות אזוריות: Votes120</h3>
                        
                        <div class="relative overflow-hidden transition-all duration-500 max-h-20" id="desc-vote">
                            <p class="text-gray-600 font-light leading-relaxed mb-4 text-sm">
                                כלי דיגיטלי ליצירת "דמיון פוליטי" ומחקר שיטות בחירות.
                                <br><br>
                                הממשק בוחן תרחישים של חלוקה אזורית בבחירות לכנסת והשפעתם על הייצוג הדמוקרטי של קבוצות אוכלוסייה שונות.
                            </p>
                        </div>
                        <button onclick="toggleDesc('vote')" class="text-xs font-bold text-gray-400 hover:text-black mb-4 flex items-center gap-1 focus:outline-none">
                            <span id="btn-text-vote">המשך...</span>
                            <svg class="w-3 h-3 transform rotate-0 transition-transform" id="icon-vote" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </button>

                        <a href="https://votes120.physital.studio/" target="_blank"
                            class="inline-flex items-center gap-2 text-xs font-black bg-black text-white px-4 py-2 hover:bg-gray-800 transition-colors">
                            <span>כלי הבחירות</span>
                            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                        </a>
                    </div>
                </article>

                <!-- Project 7: Local Culture -->
                <article class="group relative flex flex-col md:flex-row gap-8 items-start">
                    <div class="w-full md:w-1/3 aspect-[16/9] bg-gray-100 overflow-hidden border border-gray-100 relative shrink-0">
                        <img src="assets/images/merhav_new.png"
                            class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700"
                            alt="Local Culture">
                    </div>
                    <div class="w-full md:w-2/3">
                        <span class="text-[10px] font-bold uppercase tracking-widest text-gray-500 block mb-2">מועצה
                            מקומית פרדס חנה</span>
                        <h3 class="text-2xl font-black mb-3 group-hover:underline decoration-2 underline-offset-4">מהי
                            תרבות מקומית?</h3>
                        
                        <div class="relative overflow-hidden transition-all duration-500 max-h-20" id="desc-culture">
                            <p class="text-gray-600 font-light leading-relaxed mb-4 text-sm">
                                מיפוי "תרבות רכה" (Soft Culture) ושימור הזהות המקומית.
                                <br><br>
                                כלי שיתופי בו תושבים מסמנים מוקדי תרבות ליצירת מדיניות תכנון רגישה, המשלבת בין פיתוח לבין שמירה על אופיו הייחודי של המקום.
                            </p>
                        </div>
                        <button onclick="toggleDesc('culture')" class="text-xs font-bold text-gray-400 hover:text-black mb-4 flex items-center gap-1 focus:outline-none">
                            <span id="btn-text-culture">המשך...</span>
                            <svg class="w-3 h-3 transform rotate-0 transition-transform" id="icon-culture" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </button>

                        <a href="https://docs.google.com/document/d/1ri7-denCHJmmiDiUvVGPxHLL-Wbd4nO5RUUQkMDkNK8/edit"
                            target="_blank" class="inline-flex items-center gap-2 text-xs font-black bg-black text-white px-4 py-2 hover:bg-gray-800 transition-colors">
                            <span>מסמך המדיניות</span>
                            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                        </a>
                    </div>
                </article>

                <script>
                    function toggleDesc(id) {
                        const desc = document.getElementById('desc-' + id);
                        const btnText = document.getElementById('btn-text-' + id);
                        const icon = document.getElementById('icon-' + id);
                        
                        if (desc.style.maxHeight) {
                            // Collapse
                            desc.style.maxHeight = null;
                            btnText.innerText = "המשך...";
                            icon.classList.remove('rotate-180');
                        } else {
                            // Expand
                            desc.style.maxHeight = desc.scrollHeight + "px";
                            btnText.innerText = "סגור";
                            icon.classList.add('rotate-180');
                        }
                    }
                </script>

            </div>"""

start_pos = content.find(start_marker)
if start_pos == -1:
    print(f"Start marker not found: {start_marker}")
    # Try finding without attributes just in case
    start_marker_alt = '<div class="grid grid-cols-1 gap-y-24">'
    start_pos = content.find(start_marker_alt)
    if start_pos == -1:
        print("Alt start marker not found either.")
        exit(1)

# Find end marker
# The section is followed by Section 06 which starts with:
# <hr class="border-gray-100 mb-40">
end_marker_str = '<hr class="border-gray-100 mb-40">'
end_pos = content.find(end_marker_str, start_pos)

if end_pos == -1:
    print(f"End marker not found: {end_marker_str}")
    # Alternative: find just the HR
    end_marker_str = '<hr class="border-gray-100 mb-40">'
    end_pos = content.find(end_marker_str, start_pos)
    if end_pos == -1:
      print("Alt end marker not found")
      exit(1)

# Look for the closing div of the grid *before* the HR
# Actually, if we just replace from start_marker to end_pos, we also likely capture the </div> closing the grid.
# The new content ends with </div> using string concatenation, so we should be good.

# Wait, we need to be careful if there are extra whitespaces between the last </div> and the <hr>.
# Let's inspect the file content around end_pos to be sure.
print(f"Content around end_pos: {content[end_pos-50:end_pos+50]}")

# Perform replacement
updated_content = content[:start_pos] + new_content + "\n            </section>\n\n            " + content[end_pos:]

# Wait, I see </section> in my splice above. I need to make sure I don't double close or miss close.
# The original code had:
# </div>
# </section>
# <hr ...>

# My new_content ends with </div>.
# So I should append </section> and then the rest.

# Let's write the file.
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(updated_content)

print("Successfully updated index.html via script.")
