# Case Study: UpgradeDjango.com

![right fit](screenshots/upgradedjango.png)

![inline](qrcodes/upgradedjango.png)

https://UpgradeDjango.com

---

There should be one easy and obvious to know which version of Django to use.

![inline](screenshots/upgradedjango.png)

---

- Built by humans
- Maintained by Claude Code
- Built with Hugo: https://gohugo.io

---

## Hugo for DjangoUpgrade.com

- Static website generator
- Single binary file - no dependencies
- Cross-platform compatibility
- No-code solution for static hosting
- Alternative to Ruby/Python generators

---

# Big Unlock: URL Reading

## Beyond File Operations

- Instead of: "Open this JSON file"
- Better: "Read this website URL"
- Claude Code can fetch and parse web content
- Update local files based on live data

---

# Django security release blog post

![inline](screenshots/upgradedjango-security-releases.png)

---

# Our prompt

> Please read https://www.djangoproject.com/weblog/2025/oct/01/security-releases/ and then update our Django 5.2, 5.1, and 4.2 files.

![inline](qrcodes/upgradedjango-security-releases.png)

---

### Demo

![inline](screenshots/upgradedjango-claude-code.png)

---

# Code Changes

![inline](screenshots/upgradedjango-diff.png)

--- 

```diff
diff --git a/data/releases/5.2.json b/data/releases/5.2.json
index 9955141..f283b22 100644
--- a/data/releases/5.2.json
+++ b/data/releases/5.2.json
@@ -8,7 +8,7 @@
     "released": "2025-04-02",
     "end_of_support": "2028-04-01",
     "end_of_extended_support": "2029-04-01",
-    "latest_release": "5.2.5",
+    "latest_release": "5.2.7",
     "python_versions": [
         "3.10",
         "3.11",
@@ -16,6 +16,22 @@
         "3.13"
     ],
     "versions": [
+        {
+            "version": "5.2.7",
+            "released": "2025-10-01",
+            "release_type": "security",
+            "github_url": "https://github.com/django/django/releases/tag/5.2.7",
+            "release_notes_url": "https://docs.djangoproject.com/en/dev/releases/5.2.7/",
+            "blog_post_url": "https://www.djangoproject.com/weblog/2025/oct/01/security-releases/"
+        },
+        {
+            "version": "5.2.6",
+            "released": "2025-09-03",
+            "release_type": "bugfix",
+            "github_url": "https://github.com/django/django/releases/tag/5.2.6",
+            "release_notes_url": "https://docs.djangoproject.com/en/dev/releases/5.2.6/",
+            "blog_post_url": "https://www.djangoproject.com/weblog/2025/sep/03/bugfix-releases/"
+        },
         {
             "version": "5.2.5",
             "released": "2025-08-06",
```
