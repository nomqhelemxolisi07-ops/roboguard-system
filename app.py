<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zim Primary Online Admission Portal</title>
    <style>
        /* CSS styling to make the site colorful and beautiful */
        body { 
            font-family: 'Segoe UI', Arial, sans-serif; 
            background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%); 
            margin: 0; 
            padding: 20px; 
            color: #1e293b; 
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .portal-container { 
            max-width: 550px; 
            width: 100%;
            background: #ffffff; 
            padding: 30px; 
            border-radius: 16px; 
            box-shadow: 0 10px 25px rgba(2, 132, 199, 0.15); 
            border-top: 8px solid #0284c7; 
        }
        .header-section {
            text-align: center;
            margin-bottom: 25px;
        }
        h2 { 
            color: #0369a1; 
            margin: 0 0 8px 0; 
            font-size: 26px; 
            letter-spacing: -0.5px;
        }
        .sub-tag { 
            background-color: #f0fdf4; 
            color: #166534; 
            padding: 6px 12px; 
            border-radius: 20px; 
            font-size: 13px; 
            font-weight: bold; 
            display: inline-block;
            border: 1px solid #bbf7d0;
        }
        .form-group { 
            margin-bottom: 18px; 
        }
        label { 
            display: block; 
            font-weight: 600; 
            margin-bottom: 6px; 
            font-size: 14px; 
            color: #334155; 
        }
        input, select, textarea { 
            width: 100%; 
            padding: 12px; 
            border: 2px solid #cbd5e1; 
            border-radius: 8px; 
            box-sizing: border-box; 
            font-size: 15px; 
            outline: none;
            transition: 0.2s;
        }
        input:focus, select:focus, textarea:focus {
            border-color: #0284c7;
            box-shadow: 0 0 0 4px rgba(2, 132, 199, 0.15);
        }
        .row-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }
        textarea { 
            resize: none; 
            height: 75px; 
        }
        .btn-submit { 
            width: 100%; 
            background-color: #16a34a; 
            color: white; 
            padding: 15px; 
            font-size: 16px; 
            font-weight: bold; 
            border-radius: 8px; 
            border: none; 
            cursor: pointer; 
            margin-top: 10px; 
            box-shadow: 0 4px 6px rgba(22, 163, 74, 0.2);
            transition: 0.2s; 
        }
        .btn-submit:hover { 
            background-color: #15803d; 
            box-shadow: 0 6px 12px rgba(22, 163, 74, 0.3);
        }
    </style>
</head>
<body>

<div class="portal-container">
    <div class="header-section">
        <h2>🏫 Online Admission Portal</h2>
        <div class="sub-tag">🇿🇼 Official Primary School Application</div>
    </div>

    <!-- Parent Input Fields -->
    <div class="form-group">
        <label>Child's Full Name:</label>
        <input type="text" id="childName" placeholder="e.g., Thabani Moyo">
    </div>

    <div class="row-grid">
        <div class="form-group">
            <label>Applying For Level:</label>
            <select id="gradeLevel">
                <option value="ECD A">ECD A</option>
                <option value="ECD B">ECD B</option>
                <option value="Grade 1">Grade 1</option>
                <option value="Grade 2">Grade 2</option>
                <option value="Grade 3">Grade 3</option>
                <option value="Grade 4">Grade 4</option>
                <option value="Grade 5">Grade 5</option>
                <option value="Grade 6">Grade 6</option>
                <option value="Grade 7">Grade 7</option>
            </select>
        </div>

        <div class="form-group">
            <label>Parent Phone Number:</label>
            <input type="tel" id="parentPhone" placeholder="e.g., 0772123456">
        </div>
    </div>

    <div class="form-group">
        <label>Previous School Attended (If any):</label>
        <input type="text" id="prevSchool" placeholder="e.g., Cowdray Park Primary">
    </div>

    <div class="form-group">
        <label>Latest Academic Performance / Exam Units:</label>
        <textarea id="results" placeholder="e.g., Shona: 1 unit, English: 2 units, Maths: 3 units. Total: 6 Units."></textarea>
    </div>

    <!-- Trigger Button -->
    <button class="btn-submit" onclick="sendApplication()">📩 Send Application to Admin</button>
</div>

<script>
    function sendApplication() {
        // 1. Capture the input values
        let name = document.getElementById('childName').value.trim();
        let grade = document.getElementById('gradeLevel').value;
        let phone = document.getElementById('parentPhone').value.trim();
        let oldSchool = document.getElementById('prevSchool').value.trim() || "None (First Time Enrollment)";
        let childResults = document.getElementById('results').value.trim();

        // 2. Data Validation
        if (!name || !phone || !childResults) {
            alert("❌ Please enter the Child's Name, Phone Number, and Results before sending.");
            return;
        }

        // 3. TARGET ADMIN EMAIL: Change this to the school's actual headmaster/admin email address
        let schoolAdminEmail = "headmaster.chitepo_primary@gmail.com"; 

        // 4. Constructing the Email Subject and Message Body
        let subject = encodeURIComponent(`ADMISSION REQUEST: ${name} [${grade}]`);
        
        let bodyText = `Official School Admission Application\n` +
                       `====================================\n\n` +
                       `Dear School Administrator / Headmaster,\n\n` +
                       `A parent has submitted an online enrollment request for your review.\n\n` +
                       `--- STUDENT RECORD ---\n` +
                       `• Full Name: ${name}\n` +
                       `• Level Applied: ${grade}\n` +
                       `• Previous School: ${oldSchool}\n` +
                       `• Academic Performance: ${childResults}\n\n` +
                       `--- CONTACT INFORMATION ---\n` +
                       `• Parent/Guardian Phone: ${phone}\n\n` +
                       `Please reply to this email to notify the parent of their acceptance status.\n\n` +
                       `Regards,\n` +
                       `Online Enrollment System`;
        
        let body = encodeURIComponent(bodyText);

        // 5. Native Action: Launches the device email client addressed directly to the admin
        window.location.href = `mailto:${schoolAdminEmail}?subject=${subject}&body=${body}`;
    }
</script>

</body>
</html>

