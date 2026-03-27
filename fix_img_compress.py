with open('app.py', 'r') as f:
    content = f.read()

old = '''                    <script>
                    function loadCertPhoto(input) {
                        var file = input.files[0];
                        if (!file) return;
                        var reader = new FileReader();
                        reader.onload = function(e) {
                            document.getElementById("cert-preview").src = e.target.result;
                            document.getElementById("cert-preview").style.display = "block";
                            document.getElementById("cert-doc-data").value = e.target.result.split(",")[1];
                        };
                        reader.readAsDataURL(file);
                    }
                    </script>'''

new = '''                    <script>
                    function loadCertPhoto(input) {
                        var file = input.files[0];
                        if (!file) return;
                        var reader = new FileReader();
                        reader.onload = function(e) {
                            var img = new Image();
                            img.onload = function() {
                                var canvas = document.createElement("canvas");
                                var maxSize = 1200;
                                var w = img.width, h = img.height;
                                if (w > maxSize || h > maxSize) {
                                    if (w > h) { h = h * maxSize / w; w = maxSize; }
                                    else { w = w * maxSize / h; h = maxSize; }
                                }
                                canvas.width = w;
                                canvas.height = h;
                                canvas.getContext("2d").drawImage(img, 0, 0, w, h);
                                var compressed = canvas.toDataURL("image/jpeg", 0.7);
                                document.getElementById("cert-preview").src = compressed;
                                document.getElementById("cert-preview").style.display = "block";
                                document.getElementById("cert-doc-data").value = compressed.split(",")[1];
                            };
                            img.src = e.target.result;
                        };
                        reader.readAsDataURL(file);
                    }
                    </script>'''

if old in content:
    content = content.replace(old, new)
    print("Billedkomprimering tilføjet!")
else:
    print("IKKE FUNDET")

with open('app.py', 'w') as f:
    f.write(content)
