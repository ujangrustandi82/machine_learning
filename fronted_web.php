<!DOCTYPE html>
<html>
<head>
<title>Prediksi Harga Rumah</title>
<script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="p-6">


<h2 class="text-xl font-bold mb-4">Prediksi Harga Rumah</h2>


<form id="houseForm">
<label>Luas Bangunan (m²)</label><br>
<input type="number" id="luas" required class="border p-2"><br><br>
<button type="submit" class="bg-blue-500 text-white px-4 py-2">Prediksi</button>
</form>


<div id="result" class="mt-4 font-semibold"></div>


<script>
document.getElementById('houseForm').addEventListener('submit', async function(e) {
e.preventDefault();
const luas = document.getElementById('luas').value;


const response = await fetch('http://localhost:8000/predict', {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify({ luas_bangunan: luas })
});


const data = await response.json();
document.getElementById('result').innerText = 'Perkiraan Harga Rumah: ' + data.harga_rumah + ' juta rupiah';
});
</script>


</body>
</html>
