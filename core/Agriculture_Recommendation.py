import csv

# Dictionary kinh nghiệm nông nghiệp dựa trên mã điều kiện thời tiết
agri_experience = {
    0: {  # Trời quang đãng
        "Ngô": "Trời quang, nắng ấm, nên bón phân cân đối, tưới nước đủ ẩm, chú ý theo dõi sâu bệnh.",
        "Lúa gạo": "Thời tiết lý tưởng để thúc đẩy sinh trưởng, bón phân đạm, tăng cường thoáng khí ruộng.",
        "Bông": "Cần giữ đất đủ ẩm, tưới nước đều, tránh sâu bệnh như rầy bông.",
        "Đậu tương": "Khí hậu thuận lợi, tăng cường bón phân kali, kiểm soát sâu bệnh đậu.",
        "Rau màu": "Duy trì tưới nước hợp lý, tăng cường bón phân hữu cơ, thu hoạch đúng kỳ."
    },
    1: {  # Mây ít
        "Ngô": "Mây ít làm nhiệt độ dịu hơn, giảm tưới nước, tập trung vào chăm sóc bộ rễ.",
        "Lúa gạo": "Tăng cường bón phân lân, giữ độ ẩm đất, phòng bệnh đạo ôn.",
        "Bông": "Mây ít giúp cây quang hợp hiệu quả, hạn chế sâu bướm, kiểm tra lá thường xuyên.",
        "Đậu tương": "Đạm và kali cần được cung cấp cân đối, tưới nước vừa phải.",
        "Rau màu": "Thích hợp cho phát triển thân lá, chú ý phòng bệnh héo rũ."
    },
    2: {  # Mây rải rác
        "Ngô": "Mây rải rác giúp duy trì nhiệt độ ổn định, giữ ẩm tốt, tưới nước vừa đủ.",
        "Lúa gạo": "Chú ý giữ ẩm đất, bổ sung phân kali, phòng trừ rầy nâu.",
        "Bông": "Cây phát triển ổn định, cần kiểm soát cỏ dại, phòng trừ sâu hại.",
        "Đậu tương": "Duy trì tưới nước đều, bón phân cân đối, tránh thối rễ.",
        "Rau màu": "Phù hợp cho cây phát triển, thu hoạch đúng vụ, chú ý thoát nước."
    },
    3: {  # Mây nhiều
        "Ngô": "Mây nhiều có thể làm giảm quang hợp, hạn chế bón phân đạm, tăng kiểm soát sâu bệnh.",
        "Lúa gạo": "Tăng cường thông thoáng ruộng, giảm lượng nước tưới để tránh ngập úng.",
        "Bông": "Phòng trừ bệnh phấn trắng và rệp sáp, tránh tưới quá nhiều.",
        "Đậu tương": "Cẩn trọng với bệnh hại do ẩm, giảm bón phân đạm.",
        "Rau màu": "Giữ đất thoáng khí, tưới nước hạn chế, chú ý phòng bệnh nấm."
    },
    45: {  # Sương mù
        "Ngô": "Sương mù lâu ngày làm tăng độ ẩm, chú ý phòng bệnh đạo ôn, hạn chế bón phân đạm.",
        "Lúa gạo": "Phòng bệnh đạo ôn, tránh bón phân khi trời ẩm thấp.",
        "Bông": "Tăng cường kiểm tra sâu bệnh, tránh tưới nước lúc sương mù.",
        "Đậu tương": "Chú ý phòng bệnh phấn trắng và rầy nâu.",
        "Rau màu": "Giữ đất không quá ẩm, tránh tưới nhiều."
    },
    48: {  # Sương mù đóng băng
        "Ngô": "Thời tiết cực kỳ khắc nghiệt, hạn chế tối đa tưới nước, chuẩn bị chống rét.",
        "Lúa gạo": "Chuẩn bị che chắn ruộng, tăng cường bón phân kali giúp cây chịu lạnh.",
        "Bông": "Tập trung bảo vệ cây khỏi rét, giảm bón phân đạm.",
        "Đậu tương": "Phòng chống rét bằng che phủ, giảm bón phân đạm.",
        "Rau màu": "Thu hoạch sớm, hạn chế tưới, tăng cường che chắn."
    },
    51: {  # Mưa phùn nhẹ
        "Ngô": "Mưa phùn nhẹ giúp giữ ẩm đất, giảm tưới nước, chú ý phòng bệnh nấm.",
        "Lúa gạo": "Tăng cường kiểm soát sâu bệnh, hạn chế bón phân trong ngày mưa.",
        "Bông": "Kiểm soát sâu bệnh tăng do ẩm ướt, giữ đất thoáng khí.",
        "Đậu tương": "Tưới nước giảm, chú ý phòng bệnh phấn trắng.",
        "Rau màu": "Tận dụng mưa tự nhiên, tránh tưới quá nhiều."
    },
    53: {  # Mưa phùn vừa
        "Ngô": "Mưa phùn vừa đủ, chú ý thoát nước để tránh úng.",
        "Lúa gạo": "Theo dõi bệnh đạo ôn, hạn chế bón phân đạm.",
        "Bông": "Tăng cường phòng bệnh, giữ đất thoáng khí.",
        "Đậu tương": "Kiểm soát độ ẩm đất, chú ý sâu bệnh.",
        "Rau màu": "Tránh tưới nhiều, giữ đất không bị ngập."
    },
    55: {  # Mưa phùn nặng
        "Ngô": "Mưa phùn nặng làm tăng nguy cơ úng ngập, cần thoát nước nhanh.",
        "Lúa gạo": "Cẩn trọng bệnh đạo ôn, giảm bón phân, chuẩn bị thu hoạch sớm.",
        "Bông": "Tăng cường kiểm tra bệnh phấn trắng, giữ đất thoáng.",
        "Đậu tương": "Giữ đất không bị úng, phòng trừ sâu bệnh.",
        "Rau màu": "Tăng cường thoát nước, hạn chế tưới thêm."
    },
    56: {  # Mưa phùn lạnh nhẹ
        "Ngô": "Thời tiết lạnh, hạn chế tưới, bón phân kali để tăng sức đề kháng.",
        "Lúa gạo": "Giữ đất đủ ẩm, phòng trừ bệnh lạnh như đạo ôn.",
        "Bông": "Phòng bệnh phấn trắng, tăng cường dinh dưỡng.",
        "Đậu tương": "Giữ đất thoáng khí, hạn chế tưới.",
        "Rau màu": "Giữ ấm đất, tránh tưới nước lạnh."
    },
    57: {  # Mưa phùn lạnh nặng
        "Ngô": "Rất lạnh, hạn chế tối đa tưới nước, chuẩn bị chống rét.",
        "Lúa gạo": "Che chắn ruộng, tăng cường kali, hạn chế bón phân đạm.",
        "Bông": "Tập trung bảo vệ cây khỏi lạnh, giảm bón phân đạm.",
        "Đậu tương": "Phòng chống rét, giảm tưới nước.",
        "Rau màu": "Thu hoạch sớm, che chắn cây."
    },
    61: {  # Mưa nhẹ
        "Ngô": "Mưa nhẹ giúp cung cấp nước, giảm tưới, phòng ngừa úng ngập.",
        "Lúa gạo": "Tăng cường phòng trừ sâu bệnh, hạn chế bón phân khi trời mưa.",
        "Bông": "Mưa nhẹ tốt nhưng cần tránh úng, kiểm tra sâu bệnh.",
        "Đậu tương": "Kiểm soát độ ẩm, chú ý bệnh hại.",
        "Rau màu": "Tận dụng mưa tự nhiên, giảm tưới."
    },
    63: {  # Mưa vừa
        "Ngô": "Mưa vừa giúp phát triển tốt, kiểm soát thoát nước để tránh úng.",
        "Lúa gạo": "Chú ý phòng bệnh rầy nâu, hạn chế bón phân đạm.",
        "Bông": "Phòng bệnh phấn trắng, thoát nước nhanh.",
        "Đậu tương": "Giữ đất thoáng khí, phòng bệnh tăng do ẩm.",
        "Rau màu": "Tăng cường thoát nước, hạn chế tưới."
    },
    65: {  # Mưa nặng
        "Ngô": "Mưa lớn dễ gây úng, chuẩn bị thoát nước, thu hoạch sớm nếu có thể.",
        "Lúa gạo": "Phòng trừ sâu bệnh, hạn chế bón phân, chuẩn bị thu hoạch.",
        "Bông": "Tăng cường kiểm tra bệnh, giữ đất thoáng khí.",
        "Đậu tương": "Giữ đất khô ráo, tránh thối rễ.",
        "Rau màu": "Tăng thoát nước, giảm tưới."
    },
    66: {  # Mưa lạnh nhẹ
        "Ngô": "Thời tiết lạnh, hạn chế tưới, bón kali để tăng sức đề kháng.",
        "Lúa gạo": "Phòng bệnh lạnh, giữ đất đủ ẩm.",
        "Bông": "Tăng cường dinh dưỡng, phòng bệnh phấn trắng.",
        "Đậu tương": "Giữ đất thoáng khí, hạn chế tưới.",
        "Rau màu": "Giữ ấm, tránh tưới nước lạnh."
    },
    67: {  # Mưa lạnh nặng
        "Ngô": "Rất lạnh, hạn chế tưới, chuẩn bị chống rét.",
        "Lúa gạo": "Che chắn ruộng, tăng kali, giảm đạm.",
        "Bông": "Giữ ấm, giảm bón phân đạm.",
        "Đậu tương": "Phòng chống rét, hạn chế tưới.",
        "Rau màu": "Thu hoạch sớm, che chắn cây."
    },
    71: {  # Tuyết rơi nhẹ
        "Ngô": "Tuyết rơi rất hiếm ở VN, nếu xảy ra thì cây cần bảo vệ khỏi lạnh, tránh bón phân.",
        "Lúa gạo": "Giữ ấm ruộng, hạn chế bón phân.",
        "Bông": "Che chắn cây, giảm bón phân.",
        "Đậu tương": "Phòng chống rét, giữ ấm.",
        "Rau màu": "Thu hoạch sớm, bảo vệ khỏi lạnh."
    },
    73: {  # Tuyết rơi vừa
        "Ngô": "Tương tự trên, bảo vệ cây tối đa, hạn chế bón phân.",
        "Lúa gạo": "Giữ ấm ruộng, giảm bón phân.",
        "Bông": "Che chắn kỹ, giảm bón phân.",
        "Đậu tương": "Phòng chống rét, giữ ấm.",
        "Rau màu": "Thu hoạch sớm, tránh hư hại."
    },
    75: {  # Tuyết rơi nặng
        "Ngô": "Gần như không thể trồng được, chuẩn bị thu hoạch hoặc bảo vệ tối đa.",
        "Lúa gạo": "Tương tự trên, giữ ấm tối đa.",
        "Bông": "Che chắn kỹ, giảm bón phân.",
        "Đậu tương": "Phòng chống rét, giữ ấm.",
        "Rau màu": "Thu hoạch khẩn cấp."
    },
    77: {  # Mưa tuyết hạt nhỏ
        "Ngô": "Giữ ấm cây, tránh tưới nước lạnh.",
        "Lúa gạo": "Giữ ấm ruộng, giảm bón phân.",
        "Bông": "Che chắn cây, hạn chế bón phân.",
        "Đậu tương": "Phòng chống rét.",
        "Rau màu": "Thu hoạch sớm."
    },
    80: {  # Mưa rào nhẹ
        "Ngô": "Mưa rào nhẹ giúp tưới tự nhiên, chú ý thoát nước, phòng bệnh.",
        "Lúa gạo": "Giữ đất đủ ẩm, phòng trừ sâu bệnh.",
        "Bông": "Tưới nước tự nhiên, tránh úng ngập.",
        "Đậu tương": "Kiểm soát độ ẩm, phòng bệnh.",
        "Rau màu": "Duy trì tưới vừa phải."
    },
    81: {  # Mưa rào vừa
        "Ngô": "Mưa vừa giúp cây phát triển, thoát nước tốt để tránh úng.",
        "Lúa gạo": "Chú ý phòng bệnh rầy nâu, hạn chế bón phân.",
        "Bông": "Phòng bệnh phấn trắng, giữ đất thoáng.",
        "Đậu tương": "Giữ đất khô ráo, hạn chế tưới.",
        "Rau màu": "Tăng cường thoát nước."
    },
    82: {  # Mưa rào nặng
        "Ngô": "Mưa nặng dễ gây úng, tăng thoát nước, thu hoạch sớm nếu có thể.",
        "Lúa gạo": "Phòng sâu bệnh, hạn chế bón phân.",
        "Bông": "Kiểm soát bệnh, giữ đất thoáng.",
        "Đậu tương": "Tránh thối rễ.",
        "Rau màu": "Tăng thoát nước, giảm tưới."
    },
    85: {  # Mưa tuyết rào nhẹ
        "Ngô": "Giữ ấm cây, tránh tưới nước lạnh.",
        "Lúa gạo": "Giữ ấm ruộng, giảm bón phân.",
        "Bông": "Che chắn cây, hạn chế bón phân.",
        "Đậu tương": "Phòng chống rét.",
        "Rau màu": "Thu hoạch sớm."
    },
    86: {  # Mưa tuyết rào nặng
        "Ngô": "Rất lạnh, chuẩn bị chống rét, hạn chế tưới.",
        "Lúa gạo": "Che chắn kỹ, tăng kali, giảm đạm.",
        "Bông": "Giữ ấm, giảm bón phân.",
        "Đậu tương": "Phòng chống rét.",
        "Rau màu": "Thu hoạch khẩn cấp."
    },
    95: {  # Giông bão nhẹ hoặc vừa
        "Ngô": "Chống gió, chuẩn bị thu hoạch sớm nếu có thể.",
        "Lúa gạo": "Thu hoạch nhanh, giữ đất ráo.",
        "Bông": "Giữ cây chắc chắn, giảm bón phân.",
        "Đậu tương": "Chống chịu gió, phòng trừ sâu bệnh.",
        "Rau màu": "Thu hoạch sớm, bảo vệ cây."
    },
    96: {  # Giông có mưa đá nhẹ
        "Ngô": "Rủi ro cao, thu hoạch ngay, chống gió tối đa.",
        "Lúa gạo": "Thu hoạch khẩn cấp, bảo vệ cây.",
        "Bông": "Giảm bón phân, bảo vệ cây.",
        "Đậu tương": "Rà soát, thu hoạch sớm.",
        "Rau màu": "Che chắn kịp thời."
    },
    99: {  # Giông có mưa đá nặng
        "Ngô": "Nguy hiểm, thu hoạch tối đa, chống gió bão tối đa.",
        "Lúa gạo": "Thu hoạch khẩn cấp, bảo vệ khỏi hư hại.",
        "Bông": "Giảm bón phân, bảo vệ cây.",
        "Đậu tương": "Rà soát, thu hoạch sớm.",
        "Rau màu": "Che chắn kịp thời."
    },
}


# Các loại cây
crops = ["Ngô", "Lúa gạo", "Bông", "Đậu tương", "Rau màu"]

# Tên file CSV
csv_file = "../app/controllers/Agriculture_Exp.csv"

# Viết dữ liệu ra file CSV
with open(csv_file, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    # Header
    writer.writerow(["Code", "Description"] + crops)

    # Bản đồ mã điều kiện thời tiết sang mô tả (để in ra CSV)
    weather_condition_map = {
        0: "Trời quang đãng",
        1: "Mây ít",
        2: "Mây rải rác",
        3: "Mây nhiều",
        45: "Sương mù",
        48: "Sương mù đóng băng",
        51: "Mưa phùn nhẹ",
        53: "Mưa phùn vừa",
        55: "Mưa phùn nặng",
        56: "Mưa phùn lạnh nhẹ",
        57: "Mưa phùn lạnh nặng",
        61: "Mưa nhẹ",
        63: "Mưa vừa",
        65: "Mưa nặng",
        66: "Mưa lạnh nhẹ",
        67: "Mưa lạnh nặng",
        71: "Tuyết rơi nhẹ",
        73: "Tuyết rơi vừa",
        75: "Tuyết rơi nặng",
        77: "Mưa tuyết hạt nhỏ",
        80: "Mưa rào nhẹ",
        81: "Mưa rào vừa",
        82: "Mưa rào nặng",
        85: "Mưa tuyết rào nhẹ",
        86: "Mưa tuyết rào nặng",
        95: "Giông bão nhẹ hoặc vừa",
        96: "Giông có mưa đá nhẹ",
        99: "Giông có mưa đá nặng"
    }

    # Ghi từng dòng: mã, tên điều kiện, kinh nghiệm từng cây
    for code, weather_name in weather_condition_map.items():
        exp = agri_experience.get(code, {})
        row = [code, weather_name] + [exp.get(crop, "") for crop in crops]
        writer.writerow(row)

print(f"Đã tạo file '{csv_file}' với kinh nghiệm nông nghiệp dựa trên điều kiện thời tiết.")
