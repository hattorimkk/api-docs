#!/usr/bin/env python3
import shutil, os, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_work/u101_dry_run.md")
DST = os.path.join(ROOT, "docs/08-use-cases/use-case-tao-chien-dich-p1.md")

print(f"Copying {SRC} to {DST}...")
shutil.copyfile(SRC, DST)
print("File successfully written!")

# Run validation
print("\nRunning validate.py u101...")
res = subprocess.run(["python3", os.path.join(ROOT, "_scripts/validate.py"), "u101"], capture_output=True, text=True)
print(res.stdout)
if res.stderr:
    print("STDERR:", res.stderr)

assert res.returncode == 0, "Validation failed!"
print("VALIDATION PASSED PERFECTLY!")
