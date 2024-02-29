### Breast Planning

#### Useful documents
- TP-PRT-1  Treatment planning protocols
- TP-GD-63  Planning Breast/SFX/Axilla IMRT
- TP-GD-92  Planning Breast IMRT
- TP-CP-1  Breast clinical protocol
- TP-CP-3  SCF/AX clinical protocol


Remember:

- Delete reference point location
- Delete MLCs from setup fields

### Split carriage for large fields (X>14cm)

First, check whether it is possible to move the isocentre in order to not produce a plan where X>14cm.  Moving the isocentre may negate the need for this. Alternatively a small reduction in flash, particularly for breath hold patients, may be preferable.

An X field size of 14cm will require the use of split carriages and result in the following message when the plan is calculated
!["split field warning message"](../images/split_field.png)

Once the plan has been optimised, set the plan to "Planning Approved" to create the sub fields and then back to "Unapproved". Rename the split fields appropriately e.g. RT LAT ANT and RT LAT POST.

Check that the MLC motion looks reasonable. It is known to occasionally produce weird leaf motions.

[up](README.md)

[top](../README.md)
