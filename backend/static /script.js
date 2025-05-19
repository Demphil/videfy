document.getElementById("videoForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  
  const form = e.target;
  const formData = new FormData(form);

  const resultDiv = document.getElementById("result");
  resultDiv.innerHTML = "⏳ جاري المعالجة...";

  try {
    const res = await fetch("/process", {
      method: "POST",
      body: formData
    });

    const data = await res.json();

    if (data.url) {
      resultDiv.innerHTML = `<p>✅ تمت المعالجة!</p><video src="${data.url}" controls width="100%"></video>`;
    } else {
      resultDiv.innerHTML = `<p>⚠️ حدث خطأ: ${data.error || "خطأ غير معروف"}</p>`;
    }
  } catch (err) {
    resultDiv.innerHTML = `<p>❌ فشل الاتصال بالخادم</p>`;
  }
});
