import csv, structureToolsM1BIBS, freesasa

pdb = structureToolsM1BIBS.PDB_parser("Dim_Tet_interfaces/1lvl_inter.pdb")

surface = []
interface = []
for res in pdb['A']["reslist"]:
    dejamis = False
    for atom in pdb['A'][res]["atomlist"]:
        if dejamis == False:
            if pdb['A'][res][atom]["bfactor"] == '1.00':
                interface.append(res)
                dejamis = True
            elif pdb['A'][res][atom]["bfactor"] == '0.00':
                surface.append(res)
                dejamis = True

with open('tailleSurfaceInterface_1lvl.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(['taille_surface', 'taille_interface'])
    write.writerow([str(len(surface)), str(len(interface))])

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
for i in range(0, len(interface)):
    if pdb['A'][str(interface[i])]["resname"] == 'ALA':
        ALA_i += 1
    if pdb['A'][str(interface[i])]["resname"] == 'CYS':
        CYS_i += 1
    if pdb['A'][str(interface[i])]["resname"] == 'ASP':
        ASP_i += 1
    if pdb['A'][str(interface[i])]["resname"] == 'GLU':
        GLU_i += 1
    if pdb['A'][str(interface[i])]["resname"] == 'PHE':
        PHE_i += 1
    if pdb['A'][str(interface[i])]["resname"] == 'GLY':
        GLY_i += 1
    if pdb['A'][str(interface[i])]["resname"] == 'HIS':
        HIS_i += 1
    if pdb['A'][str(interface[i])]["resname"] == 'ILE':
        ILE_i += 1
    if pdb['A'][str(interface[i])]["resname"] == 'LYS':
        LYS_i += 1
    if pdb['A'][str(interface[i])]["resname"] == 'LEU':
        LEU_i += 1
    if pdb['A'][str(interface[i])]["resname"] == 'MET':
        MET_i += 1
    if pdb['A'][str(interface[i])]["resname"] == 'ASN':
        ASN_i += 1
    if pdb['A'][str(interface[i])]["resname"] == 'PRO':
        PRO_i += 1
    if pdb['A'][str(interface[i])]["resname"] == 'GLN':
        GLN_i += 1
    if pdb['A'][str(interface[i])]["resname"] == 'ARG':
        ARG_i += 1
    if pdb['A'][str(interface[i])]["resname"] == 'SER':
        SER_i += 1
    if pdb['A'][str(interface[i])]["resname"] == 'THR':
        THR_i += 1
    if pdb['A'][str(interface[i])]["resname"] == 'VAL':
        VAL_i += 1
    if pdb['A'][str(interface[i])]["resname"] == 'TRP':
        TRP_i += 1
    if pdb['A'][str(interface[i])]["resname"] == 'TYR':
        TYR_i += 1

with open('freqAASurfaceInterface_1lvl.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(['Frequences des 20 aa a la surface et a l interface'])
    write.writerow(['acide_amine', 'frequence_surface', 'frequence_interface'])
    write.writerow(['ALA', str(ALA_s), str(ALA_i)])
    write.writerow(['CYS', str(CYS_s), str(CYS_i)])
    write.writerow(['ASP', str(ASP_s), str(ASP_i)])
    write.writerow(['GLU', str(GLU_s), str(GLU_i)])
    write.writerow(['PHE', str(PHE_s), str(PHE_i)])
    write.writerow(['GLY', str(GLY_s), str(GLY_i)])
    write.writerow(['HIS', str(HIS_s), str(HIS_i)])
    write.writerow(['ILE', str(ILE_s), str(ILE_i)])
    write.writerow(['LYS', str(LYS_s), str(LYS_i)])
    write.writerow(['LEU', str(LEU_s), str(LEU_i)])
    write.writerow(['MET', str(MET_s), str(MET_i)])
    write.writerow(['ASN', str(ASN_s), str(ASN_i)])
    write.writerow(['PRO', str(PRO_s), str(PRO_i)])
    write.writerow(['GLN', str(GLN_s), str(GLN_i)])
    write.writerow(['ARG', str(ARG_s), str(ARG_i)])
    write.writerow(['SER', str(SER_s), str(SER_i)])
    write.writerow(['THR', str(THR_s), str(THR_i)])
    write.writerow(['VAL', str(VAL_s), str(VAL_i)])
    write.writerow(['TRP', str(TRP_s), str(TRP_i)])
    write.writerow(['TYR', str(TYR_s), str(TYR_i)])

HP_s = 0; POL_s = 0; CHG_s = 0; HP_i = 0; POL_i = 0; CHG_i = 0
for i in range(0, len(surface)):
    if pdb['A'][str(surface[i])]["resname"] == ('ALA' or 'VAL' or 'ILE' or 'CYS' or 'LEU' or 'MET' or 'PRO' or 'PHE' or 'TRP'):
        HP_s += 1
    if pdb['A'][str(surface[i])]["resname"] == ('GLY' or 'SER' or 'THR' or 'ASN' or 'GLN' or 'TYR'):
        POL_s += 1
    if pdb['A'][str(surface[i])]["resname"] == ('GLU' or 'HIS' or 'ASP' or 'LYS' or 'ARG'):
        CHG_s += 1

for i in range(0, len(interface)):
    if pdb['A'][str(interface[i])]["resname"] == ('ALA' or 'VAL' or 'ILE' or 'CYS' or 'LEU' or 'MET' or 'PRO' or 'PHE' or 'TRP'):
        HP_i += 1
    if pdb['A'][str(interface[i])]["resname"] == ('GLY' or 'SER' or 'THR' or 'ASN' or 'GLN' or 'TYR'):
        POL_i += 1
    if pdb['A'][str(interface[i])]["resname"] == ('GLU' or 'HIS' or 'ASP' or 'LYS' or 'ARG'):
        CHG_i += 1

with open('freqTypesAASurfaceInterface_1lvl.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(['Fréquence des résidus hydrophobes (HP) polaires (POL) et chargés (CHG) à la surface et à l interface'])
    write.writerow(['HP_surface', 'POL_surface', 'CHG_surface', 'HP_interface', 'POL_interface', 'CHG_interface'])
    write.writerow([str(HP_s), str(POL_s), str(CHG_s), str(HP_i), str(POL_i), str(CHG_i)])
