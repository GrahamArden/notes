### Updating patients for RTDS6
- Any patients who have treatment fraction from 31/3/25 onwards will need updating
- All data up to Saturday onwards already extracted
### Registration
- DOB, postcode and sex (e.g. 1-Male) are mandatory in Registration
### Course Properties
- Name (1 name) _*** must have a space ***_
- Intent is now treatment modality (1 - External Beam Radiotherapy) or (2 - Brachytherapy)
### Diagnosis work space
- Referal Decision and Category are no longer diagnoses.
- Make a note of dates and then error out (RTDS V5 to V6 as reason).  DO NOT DELETE THE ACTUAL DIAGNOSIS (The C or D cdoe)
- Check laterality is set correct (bottom right panel) : Use N/A for e.g. prostate
### Care path
- Referal recieved should be at the correct date from above (Leave this alone)
- Add referal (Referal_1) and decision (Decision_1) tasks with correct date from above
- DOFPA (Date of first planning activity). This is the date of the plan we finally use for planning.
  - Open activity capture on scan task (e.g Brain/H&N with contrast)
  - Add procdure code (see all procedure code) and find DOFPA
  - Correct to date of service and ignore
### A1 code
- Add new A1 code and copy across data from existing A1 code
- Delete existing A1 code (Make sure you delete the existing one)

#### Fields in A1 code
- Anatomical site (Generic sites removed now need finer detail). Carl will send around the full list)
- IMRT technique
- Laterality (This is the _planned_ area, use N/A for e.g. prostates)
- RT Tx priority
   - Routine for most
- RT Intent and RCR Category is on the EPMF
- Plan Type (leave for Said for now)
- Specialist RT Trt (Select as appropriate)
- Clinical Trial (Y/N)
