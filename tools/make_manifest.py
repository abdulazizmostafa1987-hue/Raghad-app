import hashlib, json, os, sys
base = os.environ.get("BASE", "")
d = "content-packs"
packs = []
for f in sorted(os.listdir(d)):
    if not f.endswith(".json") or f == "manifest.json":
        continue
    raw = open(os.path.join(d, f), "rb").read()
    data = json.loads(raw.decode("utf-8"))
    for k in ("id", "version", "status", "subjectId", "subjectName", "lessons"):
        if k not in data:
            sys.exit(f"{f}: missing field {k}")
    packs.append({"id": data["id"], "version": data["version"],
                  "url": f"{base}/{f}", "sha256": hashlib.sha256(raw).hexdigest()})
json.dump({"packs": packs}, open(os.path.join(d, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
