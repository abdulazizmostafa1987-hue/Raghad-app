# حزم المحتوى
كل حزمة ملف JSON: `id`, `version` (رقم صحيح يزيد مع كل تعديل), `status` ("published" فقط تُحمَّل),
`subjectId`, `subjectName`, `lessons` (كل درس: id, title, objectives, body, source, questions).
الأسئلة: id, type (mcq|tf), text, options, answer (فهرس), difficulty, explanation.
عند رفع/تعديل أي حزمة يولّد Action ملف `manifest.json` تلقائيًا. ضع رابطه الخام في إعدادات ولي الأمر داخل التطبيق.
