### Precautions when treating patients with a Cardiac Implanted Electronic Device (pacemaker)

- Radiotherapy Board document "Management of cancer patients receiving radiotherapy with a cardiac implanted electronisc device: A clinical guideline" is available on QPulse as RTD-RFD-4

- See also TP-GD-23 "Preparing a Plan for Patients with a Cardiac Implanted Electronic Device"

- Maximum allowable energy is 10MV (i.e. 6 MeV, 9 MeV, 6X, 10-FFF)

- Maximum cumulative dose (including from imaging):
  - Pacemaker: 2.0 Gy
  - Implantable Cardiac Defibrilator (ICD): 0.5 Gy

- Where possible any device should be CT scanned but not placed directly in the radiotherapy treatment field
- Every effort should be made to limit the cumulative dose to the device. This may be by additional shielding.
- If the leads for the device can be seen, every effort should be made to keep the leads out of the treatment field and doses limited.

- For electron profiles see commisioning report AST-COM-91 (PDD and Profile data with Dynamic Graphs.xlsx)


### Calculating dose to pacemaker in Eclipse

- Copy plan into QAPhysics course and rename appropriately
- Duplicate structure set
- Contour pacemeker (not including leads) and add PRV (0.5 cm)
- Make sure body is not forced to water
- Ensure heterogeneity correction is ON
- Calculate with fixed monitor units from original plan
