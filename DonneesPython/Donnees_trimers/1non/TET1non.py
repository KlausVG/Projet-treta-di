import csv, structureToolsM1BIBS, freesasa

pdb = structureToolsM1BIBS.PDB_parser("Dim_Tet_interfaces/1non_inter.pdb")

surface = []
interface1 = []
interface2 = []
for res in pdb['A']["reslist"]:
    dejamis = False
    for atom in pdb['A'][res]["atomlist"]:
        if dejamis == False:
            if pdb['A'][res][atom]["bfactor"] == '1.00':
                interface1.append(res)
                dejamis = True
            elif pdb['A'][res][atom]["bfactor"] == '0.00':
                surface.append(res)
                dejamis = True
            elif pdb['A'][res][atom]["bfactor"] == '2.00':
                interface2.append(res)
                dejamis = True

with open('tailleSurfaceInterfaces_1non.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(['taille_surface', 'taille_interface1', 'taille_interface2'])
    write.writerow([str(len(surface)), str(len(interface1)), str(len(interface2))])

ALA_s = 0; CYS_s = 0; ASP_s = 0; GLU_s = 0; PHE_s = 0; GLY_s = 0; HIS_s = 0; ILE_s = 0; LYS_s = 0; LEU_s = 0
MET_s = 0; ASN_s = 0; PRO_s = 0; GLN_s = 0; ARG_s = 0; SER_s = 0; THR_s = 0; VAL_s = 0; TRP_s = 0; TYR_s = 0
for i in range(0, len(surface)):
    if pdb['A'][str(surface[i])]["resname"] == 'ALA':
        ALA_s += 1
    if pdb['A'][str(surface[i])]["resname"] == 'CYS':
        CYS_s += 1
    if pdb['A'][str(surface[i])]["resname"] == 'ASP':
        ASP_s += 1
    if pdb['A'][str(surface[i])]["resname"] == 'GLU':
        GLU_s += 1
    if pdb['A'][str(surface[i])]["resname"] == 'PHE':
        PHE_s += 1
    if pdb['A'][str(surface[i])]["resname"] == 'GLY':
        GLY_s += 1
    if pdb['A'][str(surface[i])]["resname"] == 'HIS':
        HIS_s += 1
    if pdb['A'][str(surface[i])]["resname"] == 'ILE':
        ILE_s += 1
    if pdb['A'][str(surface[i])]["resname"] == 'LYS':
        LYS_s += 1
    if pdb['A'][str(surface[i])]["resname"] == 'LEU':
        LEU_s += 1
    if pdb['A'][str(surface[i])]["resname"] == 'MET':
        MET_s += 1
    if pdb['A'][str(surface[i])]["resname"] == 'ASN':
        ASN_s += 1
    if pdb['A'][str(surface[i])]["resname"] == 'PRO':
        PRO_s += 1
    if pdb['A'][str(surface[i])]["resname"] == 'GLN':
        GLN_s += 1
    if pdb['A'][str(surface[i])]["resname"] == 'ARG':
        ARG_s += 1
    if pdb['A'][str(surface[i])]["resname"] == 'SER':
        SER_s += 1
    if pdb['A'][str(surface[i])]["resname"] == 'THR':
        THR_s += 1
    if pdb['A'][str(surface[i])]["resname"] == 'VAL':
        VAL_s += 1
    if pdb['A'][str(surface[i])]["resname"] == 'TRP':
        TRP_s += 1
    if pdb['A'][str(surface[i])]["resname"] == 'TYR':
        TYR_s += 1

ALA_i = 0; CYS_i = 0; ASP_i = 0; GLU_i = 0; PHE_i = 0; GLY_i = 0; HIS_i = 0; ILE_i = 0; LYS_i = 0; LEU_i = 0
MET_i = 0; ASN_i = 0; PRO_i = 0; GLN_i = 0; ARG_i = 0; SER_i = 0; THR_i = 0; VAL_i = 0; TRP_i = 0; TYR_i = 0
for i in range(0, len(interface1)):
    if pdb['A'][str(interface1[i])]["resname"] == 'ALA':
        ALA_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == 'CYS':
        CYS_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == 'ASP':
        ASP_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == 'GLU':
        GLU_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == 'PHE':
        PHE_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == 'GLY':
        GLY_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == 'HIS':
        HIS_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == 'ILE':
        ILE_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == 'LYS':
        LYS_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == 'LEU':
        LEU_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == 'MET':
        MET_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == 'ASN':
        ASN_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == 'PRO':
        PRO_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == 'GLN':
        GLN_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == 'ARG':
        ARG_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == 'SER':
        SER_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == 'THR':
        THR_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == 'VAL':
        VAL_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == 'TRP':
        TRP_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == 'TYR':
        TYR_i += 1

ALA_i2 = 0; CYS_i2 = 0; ASP_i2 = 0; GLU_i2 = 0; PHE_i2 = 0; GLY_i2 = 0; HIS_i2 = 0; ILE_i2 = 0; LYS_i2 = 0; LEU_i2 = 0
MET_i2 = 0; ASN_i2 = 0; PRO_i2 = 0; GLN_i2 = 0; ARG_i2 = 0; SER_i2 = 0; THR_i2 = 0; VAL_i2 = 0; TRP_i2 = 0; TYR_i2 = 0
for i in range(0, len(interface2)):
    if pdb['A'][str(interface2[i])]["resname"] == 'ALA':
        ALA_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == 'CYS':
        CYS_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == 'ASP':
        ASP_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == 'GLU':
        GLU_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == 'PHE':
        PHE_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == 'GLY':
        GLY_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == 'HIS':
        HIS_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == 'ILE':
        ILE_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == 'LYS':
        LYS_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == 'LEU':
        LEU_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == 'MET':
        MET_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == 'ASN':
        ASN_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == 'PRO':
        PRO_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == 'GLN':
        GLN_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == 'ARG':
        ARG_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == 'SER':
        SER_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == 'THR':
        THR_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == 'VAL':
        VAL_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == 'TRP':
        TRP_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == 'TYR':
        TYR_i2 += 1

with open('freqAASurfaceInterfaces_1non.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(['Frequences des 20 aa a la surface et aux interfaces'])
    write.writerow(['acide_amine', 'frequence_surface', 'frequence_interface1', 'frequence_interface2'])
    write.writerow(['ALA', str(ALA_s), str(ALA_i), str(ALA_i2)])
    write.writerow(['CYS', str(CYS_s), str(CYS_i), str(CYS_i2)])
    write.writerow(['ASP', str(ASP_s), str(ASP_i), str(ASP_i2)])
    write.writerow(['GLU', str(GLU_s), str(GLU_i), str(GLU_i2)])
    write.writerow(['PHE', str(PHE_s), str(PHE_i), str(PHE_i2)])
    write.writerow(['GLY', str(GLY_s), str(GLY_i), str(GLY_i2)])
    write.writerow(['HIS', str(HIS_s), str(HIS_i), str(HIS_i2)])
    write.writerow(['ILE', str(ILE_s), str(ILE_i), str(ILE_i2)])
    write.writerow(['LYS', str(LYS_s), str(LYS_i), str(LYS_i2)])
    write.writerow(['LEU', str(LEU_s), str(LEU_i), str(LEU_i2)])
    write.writerow(['MET', str(MET_s), str(MET_i), str(MET_i2)])
    write.writerow(['ASN', str(ASN_s), str(ASN_i), str(ASN_i2)])
    write.writerow(['PRO', str(PRO_s), str(PRO_i), str(PRO_i2)])
    write.writerow(['GLN', str(GLN_s), str(GLN_i), str(GLN_i2)])
    write.writerow(['ARG', str(ARG_s), str(ARG_i), str(ARG_i2)])
    write.writerow(['SER', str(SER_s), str(SER_i), str(SER_i2)])
    write.writerow(['THR', str(THR_s), str(THR_i), str(THR_i2)])
    write.writerow(['VAL', str(VAL_s), str(VAL_i), str(VAL_i2)])
    write.writerow(['TRP', str(TRP_s), str(TRP_i), str(TRP_i2)])
    write.writerow(['TYR', str(TYR_s), str(TYR_i), str(TYR_i2)])

HP_s = 0; POL_s = 0; CHG_s = 0; HP_i = 0; POL_i = 0; CHG_i = 0; HP_i2 = 0; POL_i2 = 0; CHG_i2 = 0
for i in range(0, len(surface)):
    if pdb['A'][str(surface[i])]["resname"] == ('ALA' or 'VAL' or 'ILE' or 'CYS' or 'LEU' or 'MET' or 'PRO' or 'PHE' or 'TRP'):
        HP_s += 1
    if pdb['A'][str(surface[i])]["resname"] == ('GLY' or 'SER' or 'THR' or 'ASN' or 'GLN' or 'TYR'):
        POL_s += 1
    if pdb['A'][str(surface[i])]["resname"] == ('GLU' or 'HIS' or 'ASP' or 'LYS' or 'ARG'):
        CHG_s += 1

for i in range(0, len(interface1)):
    if pdb['A'][str(interface1[i])]["resname"] == ('ALA' or 'VAL' or 'ILE' or 'CYS' or 'LEU' or 'MET' or 'PRO' or 'PHE' or 'TRP'):
        HP_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == ('GLY' or 'SER' or 'THR' or 'ASN' or 'GLN' or 'TYR'):
        POL_i += 1
    if pdb['A'][str(interface1[i])]["resname"] == ('GLU' or 'HIS' or 'ASP' or 'LYS' or 'ARG'):
        CHG_i += 1

for i in range(0, len(interface2)):
    if pdb['A'][str(interface2[i])]["resname"] == ('ALA' or 'VAL' or 'ILE' or 'CYS' or 'LEU' or 'MET' or 'PRO' or 'PHE' or 'TRP'):
        HP_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == ('GLY' or 'SER' or 'THR' or 'ASN' or 'GLN' or 'TYR'):
        POL_i2 += 1
    if pdb['A'][str(interface2[i])]["resname"] == ('GLU' or 'HIS' or 'ASP' or 'LYS' or 'ARG'):
        CHG_i2 += 1

with open('freqTypesAASurfaceInterfaces_1non.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(['Fréquence des résidus hydrophobes (HP) polaires (POL) et chargés (CHG) à la surface et aux interfaces'])
    write.writerow(['HP_surface', 'POL_surface', 'CHG_surface', 'HP_interface1', 'POL_interface1', 'CHG_interface1', 'HP_interface2', 'POL_interface2', 'CHG_interface2'])
    write.writerow([str(HP_s), str(POL_s), str(CHG_s), str(HP_i), str(POL_i), str(CHG_i), str(HP_i2), str(POL_i2), str(CHG_i2)])
