# convert_ppm.py
def convert_p6_to_p3(input_path, output_path):
    with open(input_path, "rb") as f:
        # Header 읽기
        magic_number = f.readline().strip()
        if magic_number != b'P6':
            raise ValueError("Not a P6 PPM file.")

        # 주석 무시
        line = f.readline()
        while line.startswith(b'#'):
            line = f.readline()

        # width, height
        width_height = line.strip().split()
        width = int(width_height[0])
        height = int(width_height[1])

        max_color = int(f.readline().strip())

        # binary pixel data
        pixel_data = f.read()

    # P3 포맷으로 변환해서 저장
    with open(output_path, "w") as out:
        out.write("P3\n")
        out.write(f"{width} {height}\n")
        out.write(f"{max_color}\n")

        for i in range(0, len(pixel_data), 3):
            r = pixel_data[i]
            g = pixel_data[i+1]
            b = pixel_data[i+2]
            out.write(f"{r} {g} {b}\n")

# 실행 예
if __name__ == "__main__":
    convert_p6_to_p3("/home/data/colorP6File.ppm", "colorP3File.ppm")

