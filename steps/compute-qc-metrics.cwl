cwlVersion: v1.0
class: CommandLineTool
label: Compute QC metrics
requirements:
  DockerRequirement:
    dockerPull: hubmap/scrna-analysis:latest
baseCommand: /opt/compute_qc_metrics.py

inputs:
  assay:
    type: string
    inputBinding:
      position: 0
  h5ad_primary:
    type: File
    inputBinding:
      position: 1
  bam_file:
    type: File
    inputBinding:
      position: 2
outputs:
  scanpy_qc_results:
    type: File
    outputBinding:
      glob: qc_results.hdf5
  qc_metrics:
    type: File
    outputBinding:
      glob: alignment_qc_results.json
