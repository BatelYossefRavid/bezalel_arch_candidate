
import os

def force_update_vision():
    file_path = 'c:\\git\\bezalel_arch_candidate\\index.html'
    vision_path = 'c:\\git\\bezalel_arch_candidate\\vision_final.txt'

    # User's Rashit Davar Text (Hardcoded to match request exactly)
    rashit_davar_intro = """
    <div class="mb-24">
        <h3 class="text-3xl font-black mb-10 font-arch border-b-2 border-black pb-4 inline-block">ראשית דבר</h3>
        <div class="space-y-8 text-2xl font-light italic text-gray-800 leading-relaxed max-w-4xl">
            <p>אני זוכרת את היום שבו התקבלתי ללימודים בבצלאל. פתיחת המעטפה לא סימלה עבורי רק קבלה למסלול לימודים, אלא כניסה למרחב אינטלקטואלי שבו אדריכלות נתפסה כתחום ביקורתי, תרבותי ואזרחי. השנים בבית הספר עיצבו את שפת החשיבה שלי ואת ההבנה כי תכנון איננו רק פעולה מקצועית, אלא עמדה ביחס למציאות.</p>

            <p>המועמדות להובלת בית הספר נשענת על מסלול מקצועי ואקדמי שהחל כאן והתרחב לאורך השנים דרך מחקר, הוראה והובלה מוסדית. לימודי המחקר בלונדון והדוקטורט בטכניון חידדו אצלי את העיסוק בשאלות מערכתיות של קבלת החלטות מרחבית, תשתיות ידע וכלים דיגיטליים מתקדמים. בהמשך, שותפות בהקמת בית הספר לארכיטקטורה ב-SCE והובלת תחום הידע הדיגיטלי במסגרתו אפשרו לי לפעול בתוך מערכות אקדמיות מורכבות ולפתח תשתיות מחקר ופדגוגיה חדשות. במקביל, במסגרת NUR Lab, פיתחתי שיתופי פעולה עם רשויות תכנון, מוסדות ציבוריים ושותפים בינלאומיים.</p>

            <p>אני מגיעה לתפקיד מתוך תפיסה ביקורתית של האדריכלות כתחום ידע ופעולה, ומתוך ניסיון בעבודה עם מערכות מורכבות שבהן מרחב, מדיניות וטכנולוגיה שזורים זה בזה. ניסיון זה מעצב את הבנתי לגבי אחריותו ותפקידו של בית ספר לאדריכלות בעידן של שינוי טכנולוגי וחברתי מואץ — לא רק כמוסד הוראה, אלא כזירה לעיצוב תרבות מקצועית ושיח ציבורי.</p>

            <p>התשתית המקצועית והמחקרית שנבנתה לאורך השנים היא הבסיס שממנו אני מבקשת לפעול: לחזק את העומק הביקורתי של בית הספר, להרחיב את אופקיו הבין־תחומיים, ולבסס את מקומו כמוסד מוביל בשדה האדריכלות הישראלי והבינלאומי.</p>
        </div>
    </div>
    """

    # Read Vision Final Text
    with open(vision_path, 'r', encoding='utf-8') as f:
        vision_text_raw = f.read()

    # Format Vision Text
    paragraphs = vision_text_raw.strip().split('\n')
    vision_html = '<!-- Vision Chapters -->\n<div class="space-y-8 text-xl font-light leading-relaxed text-gray-800">\n'
    
    if paragraphs:
        title = paragraphs[0]
        vision_html += f'    <h3 class="text-3xl font-black mb-10 font-arch border-b-2 border-black pb-4 inline-block">{title}</h3>\n'
        paragraphs = paragraphs[1:]

    for p in paragraphs:
        if p.strip():
            vision_html += f'    <p>{p.strip()}</p>\n'
    vision_html += '</div>'

    # Combine
    full_section_content = f"\n{rashit_davar_intro}\n\n{vision_html}\n"

    # Read Index
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Locate Replacement Hooks
    # We want to replace everything inside the <article> tag in the Vision section (#vision)
    # Start: <article class="prose ...">
    # End: </article>
    
    article_start_tag = '<article\n                    class="prose prose-xl prose-gray font-light leading-relaxed space-y-16 max-w-none mx-auto w-full text-gray-900 pr-8 md:pr-12 border-r border-gray-200">'
    
    start_idx = content.find(article_start_tag)
    if start_idx == -1:
        # Try finding it less strictly if line breaks differ
        start_idx = content.find('id="vision"')
        if start_idx != -1:
            start_idx = content.find('<article', start_idx)
    
    if start_idx == -1:
        print("Could not find article start")
        return

    # Find the closing > of the opening tag
    content_start_idx = content.find('>', start_idx) + 1
    
    # Find closing </article>
    end_idx = content.find('</article>', content_start_idx)
    
    if end_idx == -1:
        print("Could not find article end")
        return

    # Construct new content
    new_file_content = content[:content_start_idx] + full_section_content + "\n                    " + content[end_idx:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_file_content)
    print("Force update complete.")

if __name__ == '__main__':
    force_update_vision()
