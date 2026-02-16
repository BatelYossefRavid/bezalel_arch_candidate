
import os
import re

file_path = r'c:\git\bezalel_arch_candidate\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new content blocks based on user input
# I will use a dictionary or just direct replacement for each project ID
# But first, let's update the Section 03 description (Studio description)

# Looking for the studio description.
# In the file it is around line 770: "הסטודיו הוקם מתוך הבנה..."
studio_desc_pattern = r'(<p class="text-xl font-light leading-relaxed max-w-4xl text-gray-800">).*?(</p>)'
studio_new_text = """הסטודיו הוקם בשנת 2024 כסטודיו עצמאי הפועל בצומת שבין תכנון מרחבי, דאטה ובינה מלאכותית.
                    <br><br>
                    אנו עוסקים באפיון ויישום מערכות מבוססות נתונים — דשבורדים, כלי מיפוי ותאומים דיגיטליים — עבור גופים ציבוריים, רשויות מקומיות ומוסדות מדיניות.
                    <br>
                    ליבת העשייה היא מעבר מתכנון המבוסס על מסמכים סטטיים למערכת תכנון דיגיטלית, דינמית ושקופה."""

content = re.sub(studio_desc_pattern, r'\1' + studio_new_text + r'\2', content, flags=re.DOTALL)


# Now for the projects. I will define a helper function to generate the HTML for a project card
# so I can just replace the whole block again, ensuring I get the text right.
# OR, I can use regex to replace specific parts.
# Since I just did a full replace, maybe full replace of the grid content is safer again to key off the structure.

# Let's verify the horizontal structure is what I think it is.
# Each article has `flex flex-col md:flex-row gap-8 items-start`

# I will construct the New Grid Content again.

projects = [
    {
        "id": "tama35",
        "tag": "פרויקט דגל לאומי | מינהל התכנון",
        "title": "תמ״א 35: ממסמך תכנוני למערכת חיה",
        "img": "assets/images/tama35_map_full.png",
        "desc_visible": 'תמ״א 35, שאושרה בשנת 2008, מהווה את מסגרת־העל של התכנון במדינת ישראל – מעין "מערכת הפעלה" של המרחב הלאומי.',
        "desc_hidden": 'במסגרת העבודה עם אגף התכנון המרחבי במינהל התכנון, מפותחת תפיסת המעקב והבקרה המותאמת לעידן הדיגיטלי: מערכת שמנטרת באופן רציף את תמונת המצב המרחבית.<br><br>הפרויקט מבקש להפוך את התוכנית ממסמך סטטי לכלי דינמי – מערכת המתבססת על נתונים פתוחים, מתעדכנת דרך ממשקי API, ומאפשרת לבצע חיתוכים עקביים לאורך זמן.',
        "link": "https://mavat.iplan.gov.il/d434acda-7e9c-4914-a626-ce53d83c3c68",
        "link_text": "צפה במסמכי התוכנית"
    },
    {
        "id": "participation",
        "tag": "אגף אסטרטגיה | מינהל התכנון",
        "title": "שיתוף ציבור בעידן הדיגיטלי",
        "img": "assets/images/physital_bot.png",
        "desc_visible": "במסגרת העבודה עם אגף האסטרטגיה במינהל התכנון, פותחה תפיסה מחודשת של שיתוף ציבור בעולם דיגיטלי.",
        "desc_hidden": 'הפרויקט כולל כתיבת מדריך שיתוף ציבור, אפיון מתודולוגיות עבודה, ופיתוח ארגז כלים דיגיטלי המאפשר להנגיש מידע תכנוני מורכב לציבור רחב.<br><br>בין היתר פותחה "יועצת שיתוף ציבור דיגיטלית" – כלי אינטראקטיבי המסייע למתכננים וליועצים לבנות תהליך השתתפות מותאם הקשר ושלב תכנוני.',
        "links": [
            {"url": "https://participatory-assist.physital.studio/", "text": "יועצת דיגיטלית"},
            {"url": "https://docs.google.com/document/d/1CHihdJ0MYY2Q4xYaGrJNA24AdG-xaoQ7/edit", "text": "מדריך שיתוף"}
        ]
    },
    {
        "id": "twin",
        "tag": "הדור הבא | תכנון מרחבי",
        "title": "IPlanTwin: התאום הדיגיטלי",
        "img": "assets/images/tama35_dashboard.jpg",
        "desc_visible": 'במסגרת פרויקט "הדור הבא" של מינהל התכנון, מתבצעת עבודת אפיון של התאום הדיגיטלי (Digital Twin) של מערכת התכנון בישראל.',
        "desc_hidden": 'אני מובילה צוותי עבודה להגדרת עקרונות המערכת: כיצד מייצרים מודל מרחבי חי, כיצד משלבים שכבות מידע דינמיות, וכיצד ניתן להריץ סימולציות תכנוניות.<br><br>הפרויקט מבקש להרחיב את מושג התאום הדיגיטלי מעבר למודל טכנולוגי בלבד, ולבסס אותו ככלי אסטרטגי עבור מדיניות מרחבית ארוכת טווח.',
        "status": "בפיתוח"
    },
    {
        "id": "tlv",
        "tag": "עיריית תל אביב-יפו",
        "title": "תוכנית שימור דיגיטלית",
        "img": "assets/images/digital_preservation_tlv.png",
        "desc_visible": "בשיתוף עיריית תל אביב, פותח כלי דיגיטלי לאפיון תוכנית שימור ברוטליסטית.",
        "desc_hidden": 'המערכת מאפשרת לבחון אילו מבנים ייכנסו לתוכנית השימור, ולנתח את השפעת זכויות הבנייה על המרחב העירוני.<br><br>המעבר לכלי דיגיטלי מאפשר לבצע ניתוח מרחבי מבוסס נתונים, ולהבין כיצד החלטות רגולטוריות ישפיעו על המרקם העירוני, הצפיפות והנוף הבנוי.',
        "link": "https://digital-conservation-tlv.physital.studio/",
        "link_text": "מערכת השימור"
    },
    {
        "id": "geo",
        "tag": "המכון למחשבה ישראלית",
        "title": "לקראת אזוריות חדשה",
        "img": "assets/images/regionalism_preview.png",
        "desc_visible": 'הפרויקט "לקראת אזוריות חדשה" בוחן מודלים שונים של אזוריות בישראל – מוסדיים, תכנוניים ופוליטיים.',
        "desc_hidden": 'העבודה משלבת מחקר מדיניות, מפגשים עם בעלי תפקידים מרכזיים, ופיתוח כלי דיגיטלי המאפשר לבחון תרחישים אזוריים שונים.<br><br>הכלי מאפשר להבין כיצד שינוי במבנה המרחבי עשוי להשפיע על ייצוג, משאבים ושייכות בחברה החרדית והערבית.',
        "link": "https://geodata.physital.studio/",
        "link_text": "כלי המחקר"
    },
    {
        "id": "vote",
        "tag": "המכון למחשבה ישראלית",
        "title": "בחירות אזוריות: דמיון פוליטי",
        "img": "assets/images/vote120_preview.png",
        "desc_visible": "כלי דיגיטלי שפותח עבור המכון למחשבה ישראלית ומדמה מודלים שונים של בחירות אזוריות.",
        "desc_hidden": 'באמצעות סימולציות ניתן לבחון כיצד חלוקה מרחבית חדשה עשויה לשנות את הייצוג הפוליטי ואת מבנה הכוח הארצי, וליצור "דמיון פוליטי" חדש המבוסס על המרחב.',
        "link": "https://votes120.physital.studio/",
        "link_text": "כלי הבחירות"
    },
    {
        "id": "culture",
        "tag": "מועצה מקומית פרדס חנה-כרכור",
        "title": "מהי תרבות מקומית?",
        "img": "assets/images/merhav_new.png",
        "desc_visible": 'כלי מיפוי דיגיטלי המאפשר לתושבים לסמן מוקדים של "תרבות רכה" – פעילות יומיומית, קהילתית ולא פורמלית.',
        "desc_hidden": 'הצלבת הנתונים עם שכבות תכנון עירוניות חשפה את הקשר בין מבנה המרחב לבין האפשרות לייצר קהילה ותרבות מקומית.<br><br>הפרויקט מציע מסגרת למדיניות תכנון השומרת על מרקמים חברתיים עדינים.',
        "link": "https://docs.google.com/document/d/1ri7-denCHJmmiDiUvVGPxHLL-Wbd4nO5RUUQkMDkNK8/edit",
        "link_text": "מסמך המדיניות"
    }
]

new_grid_content = '<div class="grid grid-cols-1 gap-y-12">\n'

for p in projects:
    new_grid_content += f"""
                <!-- Project: {p['title']} -->
                <article class="group relative flex flex-col md:flex-row gap-8 items-start">
                    <div class="w-full md:w-1/3 aspect-[16/9] bg-gray-100 overflow-hidden border border-gray-100 relative shrink-0">
                        <img src="{p['img']}"
                            class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700"
                            alt="{p['title']}">
                    </div>
                    <div class="w-full md:w-2/3">
                        <span class="text-[10px] font-bold uppercase tracking-widest text-gray-500 block mb-2">{p['tag']}</span>
                        <h3 class="text-2xl font-black mb-3 group-hover:underline decoration-2 underline-offset-4">{p['title']}</h3>
                        
                        <div class="relative overflow-hidden transition-all duration-500 max-h-20" id="desc-{p['id']}">
                            <p class="text-gray-600 font-light leading-relaxed mb-4 text-sm">
                                {p['desc_visible']}
                                <br><br>
                                {p['desc_hidden']}
                            </p>
                        </div>
                        <button onclick="toggleDesc('{p['id']}')" class="text-xs font-bold text-gray-400 hover:text-black mb-4 flex items-center gap-1 focus:outline-none">
                            <span id="btn-text-{p['id']}">המשך...</span>
                            <svg class="w-3 h-3 transform rotate-0 transition-transform" id="icon-{p['id']}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </button>
    """
    
    if "links" in p:
        new_grid_content += '                        <div class="flex gap-4">\n'
        for link in p['links']:
             new_grid_content += f"""                            <a href="{link['url']}" target="_blank"
                                class="inline-flex items-center gap-2 text-xs font-black bg-black text-white px-4 py-2 hover:bg-gray-800 transition-colors">
                                <span>{link['text']}</span>
                                <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                            </a>
"""
        new_grid_content += '                        </div>\n'
    elif "link" in p:
        new_grid_content += f"""                        <a href="{p['link']}" target="_blank"
                            class="inline-flex items-center gap-2 text-xs font-black bg-black text-white px-4 py-2 hover:bg-gray-800 transition-colors">
                            <span>{p['link_text']}</span>
                            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                        </a>
"""
    elif "status" in p:
        new_grid_content += f"""                        <span class="text-xs font-bold text-gray-400 cursor-not-allowed border border-gray-200 px-3 py-1">{p['status']}</span>
"""
    
    new_grid_content += """                    </div>
                </article>
"""

# Re-add script
new_grid_content += """
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

# Replace the grid
start_marker = '<div class="grid grid-cols-1 gap-y-12">'
end_marker = '</section>'

# Find start
start_pos = content.find(start_marker)
if start_pos == -1:
    print("Grid start marker not found")
    # try searching for the gap-y-24 one just in case previous update didn't switch it?
    # No, I supposedly ran the update_cards.py script which used gap-y-12.
    # checking file content again might be wise, but let's assume it worked.
    # Ah, I see in my previous tool call I printed "Successfully updated index.html via script."
    # So it should be there.
    pass

# Find end (before HR or </section>)
# The grid ends before </section>
end_pos = content.find(end_marker, start_pos)

if start_pos != -1 and end_pos != -1:
    final_content = content[:start_pos] + new_grid_content + "\n            " + content[end_pos:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("Updates applied successfully.")
else:
    print("Could not find markers to replace.")
