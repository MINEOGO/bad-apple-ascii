import os
import math

def convert_frames_to_chunks_from_root():
    TOTAL_FRAMES = 6571
    FRAMES_PER_CHUNK = 100
    INPUT_DIR = "frames-ascii"
    INPUT_FILE_PATTERN = "out%04d.jpg.txt"
    OUTPUT_DIR = "chunks"
    OUTPUT_FILE_PATTERN = "chunk_%d.txt"
    FRAME_DELIMITER = "[FRAME_BREAK]"

    if not os.path.isdir(INPUT_DIR):
        print(f"Error: Input directory '{INPUT_DIR}' not found in the current location.")
        print("Please ensure you are running this script from the root directory and the frames directory exists.")
        return

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}/")

    total_chunks = math.ceil(TOTAL_FRAMES / FRAMES_PER_CHUNK)
    print(f"Starting conversion of {TOTAL_FRAMES} frames from '{INPUT_DIR}/' into {total_chunks} chunks...")

    for chunk_index in range(1, total_chunks + 1):
        start_frame = (chunk_index - 1) * FRAMES_PER_CHUNK + 1
        end_frame = min(chunk_index * FRAMES_PER_CHUNK, TOTAL_FRAMES)
        
        chunk_data = []
        
        print(f"Processing Chunk {chunk_index}/{total_chunks} (Frames {start_frame}-{end_frame})...")

        for frame_number in range(start_frame, end_frame + 1):
            input_filename_base = INPUT_FILE_PATTERN % frame_number
            input_filepath = os.path.join(INPUT_DIR, input_filename_base)
            
            try:
                with open(input_filepath, 'r', encoding='utf-8') as f:
                    frame_content = f.read().strip()
                    chunk_data.append(frame_content)
            except FileNotFoundError:
                print(f"Warning: Frame file not found and will be skipped: {input_filepath}")
                continue

        output_filename = os.path.join(OUTPUT_DIR, OUTPUT_FILE_PATTERN % chunk_index)
        
        try:
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(FRAME_DELIMITER.join(chunk_data))
        except IOError as e:
            print(f"Error writing to file {output_filename}: {e}")
            
    print(f"\nConversion complete. {total_chunks} chunk files have been created in the '{OUTPUT_DIR}/' directory.")

if __name__ == "__main__":
    convert_frames_to_chunks_from_root()
