document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("courseForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const field = document.getElementById("field").value;
    const time = document.getElementById("time").value;

    const difficultyMap = {
     light: 2,
     moderate: 5,
     tough: 8
   };

    const difficulty = difficultyMap[document.getElementById("difficulty").value];

    const interest = 8; // Static for now, or you can add another input

    fetch("http://127.0.0.1:5000/recommend", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ interest, difficulty, field, time }),
    })
      .then((res) => res.json())
      .then((courses) => {
        const tableBody = document.getElementById("courseTableBody");
        tableBody.innerHTML = "";

        courses.forEach((course) => {
          const row = document.createElement("tr");
          row.innerHTML = `
            <td>${course.code}</td>
            <td>${course.name}</td>
            <td>${course.difficulty}</td>
            <td>${course.suitability}</td>
            <td>${course.credits}</td>
          `;
          tableBody.appendChild(row);
        });

        document.getElementById("resultSection").style.display = "block";
      })
      .catch((err) => {
        alert("Error getting recommendations.");
        console.error(err);
      });
  });
});
