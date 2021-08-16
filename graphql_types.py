import sgqlc.types


graphql_types = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

Float = sgqlc.types.Float

Int = sgqlc.types.Int

class Long(sgqlc.types.Scalar):
    __schema__ = graphql_types


String = sgqlc.types.String


########################################################################
# Input Objects
########################################################################
class Pagination(sgqlc.types.Input):
    __schema__ = graphql_types
    __field_names__ = ('index', 'size')
    index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='index')
    size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='size')



########################################################################
# Output Objects and Interfaces
########################################################################
class CredSetTagElement(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('tag_variant', 'pval', 'se', 'beta', 'post_prob', 'multisignal_method', 'log_abf', 'is95', 'is99')
    tag_variant = sgqlc.types.Field(sgqlc.types.non_null('Variant'), graphql_name='tagVariant')
    pval = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='pval')
    se = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='se')
    beta = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='beta')
    post_prob = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='postProb')
    multisignal_method = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='MultisignalMethod')
    log_abf = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='logABF')
    is95 = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='is95')
    is99 = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='is99')


class DistanceElement(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('type_id', 'source_id', 'aggregated_score', 'tissues')
    type_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='typeId')
    source_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sourceId')
    aggregated_score = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='aggregatedScore')
    tissues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DistanceTissue'))), graphql_name='tissues')


class DistanceTissue(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('tissue', 'distance', 'score', 'quantile')
    tissue = sgqlc.types.Field(sgqlc.types.non_null('Tissue'), graphql_name='tissue')
    distance = sgqlc.types.Field(Long, graphql_name='distance')
    score = sgqlc.types.Field(Float, graphql_name='score')
    quantile = sgqlc.types.Field(Float, graphql_name='quantile')


class FPredTissue(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('tissue', 'max_effect_label', 'max_effect_score')
    tissue = sgqlc.types.Field(sgqlc.types.non_null('Tissue'), graphql_name='tissue')
    max_effect_label = sgqlc.types.Field(String, graphql_name='maxEffectLabel')
    max_effect_score = sgqlc.types.Field(Float, graphql_name='maxEffectScore')


class FunctionalPredictionElement(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('type_id', 'source_id', 'aggregated_score', 'tissues')
    type_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='typeId')
    source_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sourceId')
    aggregated_score = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='aggregatedScore')
    tissues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FPredTissue))), graphql_name='tissues')


class G2VSchema(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('qtls', 'intervals', 'functional_predictions', 'distances')
    qtls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('G2VSchemaElement'))), graphql_name='qtls')
    intervals = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('G2VSchemaElement'))), graphql_name='intervals')
    functional_predictions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('G2VSchemaElement'))), graphql_name='functionalPredictions')
    distances = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('G2VSchemaElement'))), graphql_name='distances')


class G2VSchemaElement(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('id', 'source_id', 'source_label', 'source_description_overview', 'source_description_breakdown', 'pmid', 'tissues')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    source_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sourceId')
    source_label = sgqlc.types.Field(String, graphql_name='sourceLabel')
    source_description_overview = sgqlc.types.Field(String, graphql_name='sourceDescriptionOverview')
    source_description_breakdown = sgqlc.types.Field(String, graphql_name='sourceDescriptionBreakdown')
    pmid = sgqlc.types.Field(String, graphql_name='pmid')
    tissues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Tissue'))), graphql_name='tissues')


class GWASColocalisation(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('index_variant', 'study', 'beta', 'h3', 'h4', 'log2h4h3')
    index_variant = sgqlc.types.Field(sgqlc.types.non_null('Variant'), graphql_name='indexVariant')
    study = sgqlc.types.Field(sgqlc.types.non_null('Study'), graphql_name='study')
    beta = sgqlc.types.Field(Float, graphql_name='beta')
    h3 = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='h3')
    h4 = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='h4')
    log2h4h3 = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='log2h4h3')


class GWASColocalisationForQTLWithGene(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('left_variant', 'study', 'qtl_study_id', 'phenotype_id', 'tissue', 'h3', 'h4', 'log2h4h3')
    left_variant = sgqlc.types.Field(sgqlc.types.non_null('Variant'), graphql_name='leftVariant')
    study = sgqlc.types.Field(sgqlc.types.non_null('Study'), graphql_name='study')
    qtl_study_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='qtlStudyId')
    phenotype_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phenotypeId')
    tissue = sgqlc.types.Field(sgqlc.types.non_null('Tissue'), graphql_name='tissue')
    h3 = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='h3')
    h4 = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='h4')
    log2h4h3 = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='log2h4h3')


class GWASLRColocalisation(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('left_variant', 'left_study', 'right_variant', 'right_study', 'h3', 'h4', 'log2h4h3')
    left_variant = sgqlc.types.Field(sgqlc.types.non_null('Variant'), graphql_name='leftVariant')
    left_study = sgqlc.types.Field(sgqlc.types.non_null('Study'), graphql_name='leftStudy')
    right_variant = sgqlc.types.Field(sgqlc.types.non_null('Variant'), graphql_name='rightVariant')
    right_study = sgqlc.types.Field(sgqlc.types.non_null('Study'), graphql_name='rightStudy')
    h3 = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='h3')
    h4 = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='h4')
    log2h4h3 = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='log2h4h3')


class Gecko(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('genes', 'tag_variants', 'index_variants', 'studies', 'gene_tag_variants', 'tag_variant_index_variant_studies')
    genes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Gene'))), graphql_name='genes')
    tag_variants = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Variant'))), graphql_name='tagVariants')
    index_variants = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Variant'))), graphql_name='indexVariants')
    studies = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Study'))), graphql_name='studies')
    gene_tag_variants = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GeneTagVariant'))), graphql_name='geneTagVariants')
    tag_variant_index_variant_studies = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TagVariantIndexVariantStudy'))), graphql_name='tagVariantIndexVariantStudies')


class Gene(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('id', 'symbol', 'bio_type', 'description', 'chromosome', 'tss', 'start', 'end', 'fwd_strand', 'exons')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    symbol = sgqlc.types.Field(String, graphql_name='symbol')
    bio_type = sgqlc.types.Field(String, graphql_name='bioType')
    description = sgqlc.types.Field(String, graphql_name='description')
    chromosome = sgqlc.types.Field(String, graphql_name='chromosome')
    tss = sgqlc.types.Field(Long, graphql_name='tss')
    start = sgqlc.types.Field(Long, graphql_name='start')
    end = sgqlc.types.Field(Long, graphql_name='end')
    fwd_strand = sgqlc.types.Field(Boolean, graphql_name='fwdStrand')
    exons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Long))), graphql_name='exons')


class GeneForVariant(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('gene', 'variant', 'overall_score', 'qtls', 'intervals', 'functional_predictions', 'distances')
    gene = sgqlc.types.Field(sgqlc.types.non_null(Gene), graphql_name='gene')
    variant = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='variant')
    overall_score = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='overallScore')
    qtls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('QTLElement'))), graphql_name='qtls')
    intervals = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IntervalElement'))), graphql_name='intervals')
    functional_predictions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FunctionalPredictionElement))), graphql_name='functionalPredictions')
    distances = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DistanceElement))), graphql_name='distances')


class GeneTagVariant(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('gene_id', 'tag_variant_id', 'overall_score')
    gene_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='geneId')
    tag_variant_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tagVariantId')
    overall_score = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='overallScore')


class IndexVariantAssociation(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('tag_variant', 'study', 'pval', 'pval_mantissa', 'pval_exponent', 'n_total', 'n_cases', 'overall_r2', 'afr1000_gprop', 'amr1000_gprop', 'eas1000_gprop', 'eur1000_gprop', 'sas1000_gprop', 'log10_abf', 'posterior_probability', 'odds_ratio', 'odds_ratio_cilower', 'odds_ratio_ciupper', 'beta', 'beta_cilower', 'beta_ciupper', 'direction')
    tag_variant = sgqlc.types.Field(sgqlc.types.non_null('Variant'), graphql_name='tagVariant')
    study = sgqlc.types.Field(sgqlc.types.non_null('Study'), graphql_name='study')
    pval = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='pval')
    pval_mantissa = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='pvalMantissa')
    pval_exponent = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='pvalExponent')
    n_total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='nTotal')
    n_cases = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='nCases')
    overall_r2 = sgqlc.types.Field(Float, graphql_name='overallR2')
    afr1000_gprop = sgqlc.types.Field(Float, graphql_name='afr1000GProp')
    amr1000_gprop = sgqlc.types.Field(Float, graphql_name='amr1000GProp')
    eas1000_gprop = sgqlc.types.Field(Float, graphql_name='eas1000GProp')
    eur1000_gprop = sgqlc.types.Field(Float, graphql_name='eur1000GProp')
    sas1000_gprop = sgqlc.types.Field(Float, graphql_name='sas1000GProp')
    log10_abf = sgqlc.types.Field(Float, graphql_name='log10Abf')
    posterior_probability = sgqlc.types.Field(Float, graphql_name='posteriorProbability')
    odds_ratio = sgqlc.types.Field(Float, graphql_name='oddsRatio')
    odds_ratio_cilower = sgqlc.types.Field(Float, graphql_name='oddsRatioCILower')
    odds_ratio_ciupper = sgqlc.types.Field(Float, graphql_name='oddsRatioCIUpper')
    beta = sgqlc.types.Field(Float, graphql_name='beta')
    beta_cilower = sgqlc.types.Field(Float, graphql_name='betaCILower')
    beta_ciupper = sgqlc.types.Field(Float, graphql_name='betaCIUpper')
    direction = sgqlc.types.Field(String, graphql_name='direction')


class IndexVariantsAndStudiesForTagVariant(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('associations',)
    associations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TagVariantAssociation'))), graphql_name='associations')


class IntervalElement(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('type_id', 'source_id', 'aggregated_score', 'tissues')
    type_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='typeId')
    source_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sourceId')
    aggregated_score = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='aggregatedScore')
    tissues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IntervalTissue'))), graphql_name='tissues')


class IntervalTissue(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('tissue', 'quantile', 'score')
    tissue = sgqlc.types.Field(sgqlc.types.non_null('Tissue'), graphql_name='tissue')
    quantile = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='quantile')
    score = sgqlc.types.Field(Float, graphql_name='score')


class Manhattan(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('associations', 'top_overlapped_studies')
    associations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ManhattanAssociation'))), graphql_name='associations')
    top_overlapped_studies = sgqlc.types.Field('TopOverlappedStudies', graphql_name='topOverlappedStudies', args=sgqlc.types.ArgDict((
        ('page_index', sgqlc.types.Arg(Int, graphql_name='pageIndex', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )


class ManhattanAssociation(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('pval_mantissa', 'pval_exponent', 'credible_set_size', 'ld_set_size', 'total_set_size', 'variant', 'pval', 'odds_ratio', 'odds_ratio_cilower', 'odds_ratio_ciupper', 'beta', 'beta_cilower', 'beta_ciupper', 'direction', 'best_genes', 'best_coloc_genes', 'best_locus2_genes')
    pval_mantissa = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='pvalMantissa')
    pval_exponent = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='pvalExponent')
    credible_set_size = sgqlc.types.Field(Long, graphql_name='credibleSetSize')
    ld_set_size = sgqlc.types.Field(Long, graphql_name='ldSetSize')
    total_set_size = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='totalSetSize')
    variant = sgqlc.types.Field(sgqlc.types.non_null('Variant'), graphql_name='variant')
    pval = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='pval')
    odds_ratio = sgqlc.types.Field(Float, graphql_name='oddsRatio')
    odds_ratio_cilower = sgqlc.types.Field(Float, graphql_name='oddsRatioCILower')
    odds_ratio_ciupper = sgqlc.types.Field(Float, graphql_name='oddsRatioCIUpper')
    beta = sgqlc.types.Field(Float, graphql_name='beta')
    beta_cilower = sgqlc.types.Field(Float, graphql_name='betaCILower')
    beta_ciupper = sgqlc.types.Field(Float, graphql_name='betaCIUpper')
    direction = sgqlc.types.Field(String, graphql_name='direction')
    best_genes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ScoredGene'))), graphql_name='bestGenes')
    best_coloc_genes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ScoredGene'))), graphql_name='bestColocGenes')
    best_locus2_genes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ScoredGene'))), graphql_name='bestLocus2Genes')


class Metadata(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('name', 'api_version', 'data_version')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    api_version = sgqlc.types.Field(sgqlc.types.non_null('Version'), graphql_name='apiVersion')
    data_version = sgqlc.types.Field(sgqlc.types.non_null('Version'), graphql_name='dataVersion')


class Overlap(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('variant_id_a', 'variant_id_b', 'overlap_ab', 'distinct_a', 'distinct_b')
    variant_id_a = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='variantIdA')
    variant_id_b = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='variantIdB')
    overlap_ab = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='overlapAB')
    distinct_a = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='distinctA')
    distinct_b = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='distinctB')


class OverlappedInfoForStudy(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('study', 'overlapped_variants_for_studies', 'variant_intersection_set')
    study = sgqlc.types.Field('Study', graphql_name='study')
    overlapped_variants_for_studies = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OverlappedVariantsStudies'))), graphql_name='overlappedVariantsForStudies')
    variant_intersection_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='variantIntersectionSet')


class OverlappedStudy(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('study_id', 'study', 'num_overlap_loci')
    study_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='studyId')
    study = sgqlc.types.Field('Study', graphql_name='study')
    num_overlap_loci = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='numOverlapLoci')


class OverlappedVariantsStudies(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('overlaps', 'study')
    overlaps = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Overlap))), graphql_name='overlaps')
    study = sgqlc.types.Field('Study', graphql_name='study')


class PheWAS(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('total_gwasstudies', 'associations')
    total_gwasstudies = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='totalGWASStudies')
    associations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PheWASAssociation'))), graphql_name='associations')


class PheWASAssociation(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('study_id', 'eaf', 'beta', 'se', 'pval', 'n_total', 'n_cases', 'study', 'odds_ratio')
    study_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='studyId')
    eaf = sgqlc.types.Field(Float, graphql_name='eaf')
    beta = sgqlc.types.Field(Float, graphql_name='beta')
    se = sgqlc.types.Field(Float, graphql_name='se')
    pval = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='pval')
    n_total = sgqlc.types.Field(Long, graphql_name='nTotal')
    n_cases = sgqlc.types.Field(Long, graphql_name='nCases')
    study = sgqlc.types.Field('Study', graphql_name='study')
    odds_ratio = sgqlc.types.Field(Float, graphql_name='oddsRatio')


class QTLColocalisation(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('index_variant', 'gene', 'phenotype_id', 'tissue', 'qtl_study_name', 'beta', 'h3', 'h4', 'log2h4h3')
    index_variant = sgqlc.types.Field(sgqlc.types.non_null('Variant'), graphql_name='indexVariant')
    gene = sgqlc.types.Field(sgqlc.types.non_null(Gene), graphql_name='gene')
    phenotype_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phenotypeId')
    tissue = sgqlc.types.Field(sgqlc.types.non_null('Tissue'), graphql_name='tissue')
    qtl_study_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='qtlStudyName')
    beta = sgqlc.types.Field(Float, graphql_name='beta')
    h3 = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='h3')
    h4 = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='h4')
    log2h4h3 = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='log2h4h3')


class QTLElement(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('type_id', 'source_id', 'aggregated_score', 'tissues')
    type_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='typeId')
    source_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sourceId')
    aggregated_score = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='aggregatedScore')
    tissues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('QTLTissue'))), graphql_name='tissues')


class QTLTissue(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('tissue', 'quantile', 'beta', 'pval')
    tissue = sgqlc.types.Field(sgqlc.types.non_null('Tissue'), graphql_name='tissue')
    quantile = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='quantile')
    beta = sgqlc.types.Field(Float, graphql_name='beta')
    pval = sgqlc.types.Field(Float, graphql_name='pval')


class Query(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('meta', 'search', 'genes', 'gene_info', 'study_info', 'variant_info', 'studies_for_gene', 'study_locus2_gene_table', 'manhattan', 'top_overlapped_studies', 'overlap_info_for_study', 'tag_variants_and_studies_for_index_variant', 'index_variants_and_studies_for_tag_variant', 'phe_was', 'gecko', 'genes_for_variant_schema', 'genes_for_variant', 'gwas_regional', 'qtl_regional', 'study_and_lead_variant_info', 'gwas_credible_set', 'qtl_credible_set', 'colocalisations_for_gene', 'gwas_colocalisation_for_region', 'gwas_colocalisation', 'qtl_colocalisation', 'studies_and_lead_variants_for_gene', 'studies_and_lead_variants_for_gene_by_l2_g')
    meta = sgqlc.types.Field(sgqlc.types.non_null(Metadata), graphql_name='meta')
    search = sgqlc.types.Field(sgqlc.types.non_null('SearchResult'), graphql_name='search', args=sgqlc.types.ArgDict((
        ('query_string', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='queryString', default=None)),
        ('page', sgqlc.types.Arg(Pagination, graphql_name='page', default=None)),
))
    )
    genes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Gene))), graphql_name='genes', args=sgqlc.types.ArgDict((
        ('chromosome', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='chromosome', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='end', default=None)),
))
    )
    gene_info = sgqlc.types.Field(Gene, graphql_name='geneInfo', args=sgqlc.types.ArgDict((
        ('gene_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='geneId', default=None)),
))
    )
    study_info = sgqlc.types.Field('Study', graphql_name='studyInfo', args=sgqlc.types.ArgDict((
        ('study_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='studyId', default=None)),
))
    )
    variant_info = sgqlc.types.Field('Variant', graphql_name='variantInfo', args=sgqlc.types.ArgDict((
        ('variant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='variantId', default=None)),
))
    )
    studies_for_gene = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StudyForGene'))), graphql_name='studiesForGene', args=sgqlc.types.ArgDict((
        ('gene_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='geneId', default=None)),
))
    )
    study_locus2_gene_table = sgqlc.types.Field(sgqlc.types.non_null('SLGTable'), graphql_name='studyLocus2GeneTable', args=sgqlc.types.ArgDict((
        ('study_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='studyId', default=None)),
        ('variant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='variantId', default=None)),
        ('page_index', sgqlc.types.Arg(Int, graphql_name='pageIndex', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    manhattan = sgqlc.types.Field(sgqlc.types.non_null(Manhattan), graphql_name='manhattan', args=sgqlc.types.ArgDict((
        ('study_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='studyId', default=None)),
        ('page_index', sgqlc.types.Arg(Int, graphql_name='pageIndex', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    top_overlapped_studies = sgqlc.types.Field(sgqlc.types.non_null('TopOverlappedStudies'), graphql_name='topOverlappedStudies', args=sgqlc.types.ArgDict((
        ('study_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='studyId', default=None)),
        ('page_index', sgqlc.types.Arg(Int, graphql_name='pageIndex', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    overlap_info_for_study = sgqlc.types.Field(sgqlc.types.non_null(OverlappedInfoForStudy), graphql_name='overlapInfoForStudy', args=sgqlc.types.ArgDict((
        ('study_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='studyId', default=None)),
        ('study_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='studyIds', default=None)),
))
    )
    tag_variants_and_studies_for_index_variant = sgqlc.types.Field(sgqlc.types.non_null('TagVariantsAndStudiesForIndexVariant'), graphql_name='tagVariantsAndStudiesForIndexVariant', args=sgqlc.types.ArgDict((
        ('variant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='variantId', default=None)),
        ('page_index', sgqlc.types.Arg(Int, graphql_name='pageIndex', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    index_variants_and_studies_for_tag_variant = sgqlc.types.Field(sgqlc.types.non_null(IndexVariantsAndStudiesForTagVariant), graphql_name='indexVariantsAndStudiesForTagVariant', args=sgqlc.types.ArgDict((
        ('variant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='variantId', default=None)),
        ('page_index', sgqlc.types.Arg(Int, graphql_name='pageIndex', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    phe_was = sgqlc.types.Field(sgqlc.types.non_null(PheWAS), graphql_name='pheWAS', args=sgqlc.types.ArgDict((
        ('variant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='variantId', default=None)),
        ('page_index', sgqlc.types.Arg(Int, graphql_name='pageIndex', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    gecko = sgqlc.types.Field(Gecko, graphql_name='gecko', args=sgqlc.types.ArgDict((
        ('chromosome', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='chromosome', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='end', default=None)),
))
    )
    genes_for_variant_schema = sgqlc.types.Field(sgqlc.types.non_null(G2VSchema), graphql_name='genesForVariantSchema')
    genes_for_variant = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GeneForVariant))), graphql_name='genesForVariant', args=sgqlc.types.ArgDict((
        ('variant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='variantId', default=None)),
))
    )
    gwas_regional = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RegionalAssociation'))), graphql_name='gwasRegional', args=sgqlc.types.ArgDict((
        ('study_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='studyId', default=None)),
        ('chromosome', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='chromosome', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='end', default=None)),
))
    )
    qtl_regional = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RegionalAssociation'))), graphql_name='qtlRegional', args=sgqlc.types.ArgDict((
        ('study_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='studyId', default=None)),
        ('bio_feature', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='bioFeature', default=None)),
        ('phenotype_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='phenotypeId', default=None)),
        ('chromosome', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='chromosome', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='end', default=None)),
))
    )
    study_and_lead_variant_info = sgqlc.types.Field('StudiesAndLeadVariantsForGene', graphql_name='studyAndLeadVariantInfo', args=sgqlc.types.ArgDict((
        ('study_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='studyId', default=None)),
        ('variant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='variantId', default=None)),
))
    )
    gwas_credible_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CredSetTagElement))), graphql_name='gwasCredibleSet', args=sgqlc.types.ArgDict((
        ('study_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='studyId', default=None)),
        ('variant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='variantId', default=None)),
))
    )
    qtl_credible_set = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CredSetTagElement))), graphql_name='qtlCredibleSet', args=sgqlc.types.ArgDict((
        ('study_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='studyId', default=None)),
        ('variant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='variantId', default=None)),
        ('phenotype_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='phenotypeId', default=None)),
        ('bio_feature', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='bioFeature', default=None)),
))
    )
    colocalisations_for_gene = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GWASColocalisationForQTLWithGene))), graphql_name='colocalisationsForGene', args=sgqlc.types.ArgDict((
        ('gene_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='geneId', default=None)),
))
    )
    gwas_colocalisation_for_region = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GWASLRColocalisation))), graphql_name='gwasColocalisationForRegion', args=sgqlc.types.ArgDict((
        ('chromosome', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='chromosome', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='end', default=None)),
))
    )
    gwas_colocalisation = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GWASColocalisation))), graphql_name='gwasColocalisation', args=sgqlc.types.ArgDict((
        ('study_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='studyId', default=None)),
        ('variant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='variantId', default=None)),
))
    )
    qtl_colocalisation = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(QTLColocalisation))), graphql_name='qtlColocalisation', args=sgqlc.types.ArgDict((
        ('study_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='studyId', default=None)),
        ('variant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='variantId', default=None)),
))
    )
    studies_and_lead_variants_for_gene = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StudiesAndLeadVariantsForGene'))), graphql_name='studiesAndLeadVariantsForGene', args=sgqlc.types.ArgDict((
        ('gene_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='geneId', default=None)),
))
    )
    studies_and_lead_variants_for_gene_by_l2_g = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('V2DL2GRowByGene'))), graphql_name='studiesAndLeadVariantsForGeneByL2G', args=sgqlc.types.ArgDict((
        ('gene_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='geneId', default=None)),
        ('page_index', sgqlc.types.Arg(Int, graphql_name='pageIndex', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )


class RegionalAssociation(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('variant', 'pval')
    variant = sgqlc.types.Field(sgqlc.types.non_null('Variant'), graphql_name='variant')
    pval = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='pval')


class SLGRow(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('y_proba_distance', 'y_proba_interaction', 'y_proba_molecular_qtl', 'y_proba_pathogenicity', 'y_proba_model', 'has_coloc', 'distance_to_locus', 'gene')
    y_proba_distance = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yProbaDistance')
    y_proba_interaction = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yProbaInteraction')
    y_proba_molecular_qtl = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yProbaMolecularQTL')
    y_proba_pathogenicity = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yProbaPathogenicity')
    y_proba_model = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yProbaModel')
    has_coloc = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasColoc')
    distance_to_locus = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='distanceToLocus')
    gene = sgqlc.types.Field(sgqlc.types.non_null(Gene), graphql_name='gene')


class SLGTable(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('rows', 'study', 'variant')
    rows = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SLGRow))), graphql_name='rows')
    study = sgqlc.types.Field('Study', graphql_name='study')
    variant = sgqlc.types.Field('Variant', graphql_name='variant')


class ScoredGene(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('gene', 'score')
    gene = sgqlc.types.Field(sgqlc.types.non_null(Gene), graphql_name='gene')
    score = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='score')


class SearchResult(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('total_genes', 'total_variants', 'total_studies', 'genes', 'variants', 'studies')
    total_genes = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='totalGenes')
    total_variants = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='totalVariants')
    total_studies = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='totalStudies')
    genes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Gene))), graphql_name='genes')
    variants = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Variant'))), graphql_name='variants')
    studies = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Study'))), graphql_name='studies')


class StudiesAndLeadVariantsForGene(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('index_variant', 'study', 'pval', 'pval_mantissa', 'pval_exponent', 'odds_ratio', 'odds_ratio_cilower', 'odds_ratio_ciupper', 'beta', 'beta_cilower', 'beta_ciupper', 'direction')
    index_variant = sgqlc.types.Field(sgqlc.types.non_null('Variant'), graphql_name='indexVariant')
    study = sgqlc.types.Field(sgqlc.types.non_null('Study'), graphql_name='study')
    pval = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='pval')
    pval_mantissa = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='pvalMantissa')
    pval_exponent = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='pvalExponent')
    odds_ratio = sgqlc.types.Field(Float, graphql_name='oddsRatio')
    odds_ratio_cilower = sgqlc.types.Field(Float, graphql_name='oddsRatioCILower')
    odds_ratio_ciupper = sgqlc.types.Field(Float, graphql_name='oddsRatioCIUpper')
    beta = sgqlc.types.Field(Float, graphql_name='beta')
    beta_cilower = sgqlc.types.Field(Float, graphql_name='betaCILower')
    beta_ciupper = sgqlc.types.Field(Float, graphql_name='betaCIUpper')
    direction = sgqlc.types.Field(String, graphql_name='direction')


class Study(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('study_id', 'trait_reported', 'source', 'trait_efos', 'pmid', 'pub_date', 'pub_journal', 'pub_title', 'pub_author', 'has_sumstats', 'ancestry_initial', 'ancestry_replication', 'n_initial', 'n_replication', 'n_cases', 'trait_category', 'num_assoc_loci', 'n_total')
    study_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='studyId')
    trait_reported = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='traitReported')
    source = sgqlc.types.Field(String, graphql_name='source')
    trait_efos = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='traitEfos')
    pmid = sgqlc.types.Field(String, graphql_name='pmid')
    pub_date = sgqlc.types.Field(String, graphql_name='pubDate')
    pub_journal = sgqlc.types.Field(String, graphql_name='pubJournal')
    pub_title = sgqlc.types.Field(String, graphql_name='pubTitle')
    pub_author = sgqlc.types.Field(String, graphql_name='pubAuthor')
    has_sumstats = sgqlc.types.Field(Boolean, graphql_name='hasSumstats')
    ancestry_initial = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ancestryInitial')
    ancestry_replication = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='ancestryReplication')
    n_initial = sgqlc.types.Field(Long, graphql_name='nInitial')
    n_replication = sgqlc.types.Field(Long, graphql_name='nReplication')
    n_cases = sgqlc.types.Field(Long, graphql_name='nCases')
    trait_category = sgqlc.types.Field(String, graphql_name='traitCategory')
    num_assoc_loci = sgqlc.types.Field(Long, graphql_name='numAssocLoci')
    n_total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='nTotal')


class StudyForGene(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('study',)
    study = sgqlc.types.Field(sgqlc.types.non_null(Study), graphql_name='study')


class TagVariantAssociation(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('index_variant', 'study', 'pval', 'pval_mantissa', 'pval_exponent', 'n_total', 'n_cases', 'overall_r2', 'afr1000_gprop', 'amr1000_gprop', 'eas1000_gprop', 'eur1000_gprop', 'sas1000_gprop', 'log10_abf', 'posterior_probability', 'odds_ratio', 'odds_ratio_cilower', 'odds_ratio_ciupper', 'beta', 'beta_cilower', 'beta_ciupper', 'direction')
    index_variant = sgqlc.types.Field(sgqlc.types.non_null('Variant'), graphql_name='indexVariant')
    study = sgqlc.types.Field(sgqlc.types.non_null(Study), graphql_name='study')
    pval = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='pval')
    pval_mantissa = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='pvalMantissa')
    pval_exponent = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='pvalExponent')
    n_total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='nTotal')
    n_cases = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='nCases')
    overall_r2 = sgqlc.types.Field(Float, graphql_name='overallR2')
    afr1000_gprop = sgqlc.types.Field(Float, graphql_name='afr1000GProp')
    amr1000_gprop = sgqlc.types.Field(Float, graphql_name='amr1000GProp')
    eas1000_gprop = sgqlc.types.Field(Float, graphql_name='eas1000GProp')
    eur1000_gprop = sgqlc.types.Field(Float, graphql_name='eur1000GProp')
    sas1000_gprop = sgqlc.types.Field(Float, graphql_name='sas1000GProp')
    log10_abf = sgqlc.types.Field(Float, graphql_name='log10Abf')
    posterior_probability = sgqlc.types.Field(Float, graphql_name='posteriorProbability')
    odds_ratio = sgqlc.types.Field(Float, graphql_name='oddsRatio')
    odds_ratio_cilower = sgqlc.types.Field(Float, graphql_name='oddsRatioCILower')
    odds_ratio_ciupper = sgqlc.types.Field(Float, graphql_name='oddsRatioCIUpper')
    beta = sgqlc.types.Field(Float, graphql_name='beta')
    beta_cilower = sgqlc.types.Field(Float, graphql_name='betaCILower')
    beta_ciupper = sgqlc.types.Field(Float, graphql_name='betaCIUpper')
    direction = sgqlc.types.Field(String, graphql_name='direction')


class TagVariantIndexVariantStudy(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('tag_variant_id', 'index_variant_id', 'study_id', 'r2', 'posterior_probability', 'pval', 'pval_mantissa', 'pval_exponent', 'odds_ratio', 'odds_ratio_cilower', 'odds_ratio_ciupper', 'beta', 'beta_cilower', 'beta_ciupper', 'direction')
    tag_variant_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tagVariantId')
    index_variant_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='indexVariantId')
    study_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='studyId')
    r2 = sgqlc.types.Field(Float, graphql_name='r2')
    posterior_probability = sgqlc.types.Field(Float, graphql_name='posteriorProbability')
    pval = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='pval')
    pval_mantissa = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='pvalMantissa')
    pval_exponent = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='pvalExponent')
    odds_ratio = sgqlc.types.Field(Float, graphql_name='oddsRatio')
    odds_ratio_cilower = sgqlc.types.Field(Float, graphql_name='oddsRatioCILower')
    odds_ratio_ciupper = sgqlc.types.Field(Float, graphql_name='oddsRatioCIUpper')
    beta = sgqlc.types.Field(Float, graphql_name='beta')
    beta_cilower = sgqlc.types.Field(Float, graphql_name='betaCILower')
    beta_ciupper = sgqlc.types.Field(Float, graphql_name='betaCIUpper')
    direction = sgqlc.types.Field(String, graphql_name='direction')


class TagVariantsAndStudiesForIndexVariant(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('associations',)
    associations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IndexVariantAssociation))), graphql_name='associations')


class Tissue(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class TopOverlappedStudies(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('study', 'top_studies_by_loci_overlap')
    study = sgqlc.types.Field(Study, graphql_name='study')
    top_studies_by_loci_overlap = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(OverlappedStudy))), graphql_name='topStudiesByLociOverlap')


class V2DBeta(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('direction', 'beta_ci', 'beta_cilower', 'beta_ciupper')
    direction = sgqlc.types.Field(String, graphql_name='direction')
    beta_ci = sgqlc.types.Field(Float, graphql_name='betaCI')
    beta_cilower = sgqlc.types.Field(Float, graphql_name='betaCILower')
    beta_ciupper = sgqlc.types.Field(Float, graphql_name='betaCIUpper')


class V2DL2GRowByGene(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('odds', 'beta', 'pval', 'pval_exponent', 'pval_mantissa', 'y_proba_distance', 'y_proba_interaction', 'y_proba_molecular_qtl', 'y_proba_pathogenicity', 'y_proba_model', 'study', 'variant')
    odds = sgqlc.types.Field(sgqlc.types.non_null('V2DOdds'), graphql_name='odds')
    beta = sgqlc.types.Field(sgqlc.types.non_null(V2DBeta), graphql_name='beta')
    pval = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='pval')
    pval_exponent = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='pvalExponent')
    pval_mantissa = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='pvalMantissa')
    y_proba_distance = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yProbaDistance')
    y_proba_interaction = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yProbaInteraction')
    y_proba_molecular_qtl = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yProbaMolecularQTL')
    y_proba_pathogenicity = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yProbaPathogenicity')
    y_proba_model = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yProbaModel')
    study = sgqlc.types.Field(sgqlc.types.non_null(Study), graphql_name='study')
    variant = sgqlc.types.Field(sgqlc.types.non_null('Variant'), graphql_name='variant')


class V2DOdds(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('odds_ci', 'odds_cilower', 'odds_ciupper')
    odds_ci = sgqlc.types.Field(Float, graphql_name='oddsCI')
    odds_cilower = sgqlc.types.Field(Float, graphql_name='oddsCILower')
    odds_ciupper = sgqlc.types.Field(Float, graphql_name='oddsCIUpper')


class Variant(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('chromosome', 'position', 'ref_allele', 'alt_allele', 'rs_id', 'chromosome_b37', 'position_b37', 'id', 'nearest_gene', 'nearest_gene_distance', 'nearest_coding_gene', 'nearest_coding_gene_distance', 'most_severe_consequence', 'cadd_raw', 'cadd_phred', 'gnomad_afr', 'gnomad_amr', 'gnomad_asj', 'gnomad_eas', 'gnomad_fin', 'gnomad_nfe', 'gnomad_nfeest', 'gnomad_nfenwe', 'gnomad_nfeseu', 'gnomad_nfeonf', 'gnomad_oth')
    chromosome = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='chromosome')
    position = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='position')
    ref_allele = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='refAllele')
    alt_allele = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='altAllele')
    rs_id = sgqlc.types.Field(String, graphql_name='rsId')
    chromosome_b37 = sgqlc.types.Field(String, graphql_name='chromosomeB37')
    position_b37 = sgqlc.types.Field(Long, graphql_name='positionB37')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    nearest_gene = sgqlc.types.Field(Gene, graphql_name='nearestGene')
    nearest_gene_distance = sgqlc.types.Field(Long, graphql_name='nearestGeneDistance')
    nearest_coding_gene = sgqlc.types.Field(Gene, graphql_name='nearestCodingGene')
    nearest_coding_gene_distance = sgqlc.types.Field(Long, graphql_name='nearestCodingGeneDistance')
    most_severe_consequence = sgqlc.types.Field(String, graphql_name='mostSevereConsequence')
    cadd_raw = sgqlc.types.Field(Float, graphql_name='caddRaw')
    cadd_phred = sgqlc.types.Field(Float, graphql_name='caddPhred')
    gnomad_afr = sgqlc.types.Field(Float, graphql_name='gnomadAFR')
    gnomad_amr = sgqlc.types.Field(Float, graphql_name='gnomadAMR')
    gnomad_asj = sgqlc.types.Field(Float, graphql_name='gnomadASJ')
    gnomad_eas = sgqlc.types.Field(Float, graphql_name='gnomadEAS')
    gnomad_fin = sgqlc.types.Field(Float, graphql_name='gnomadFIN')
    gnomad_nfe = sgqlc.types.Field(Float, graphql_name='gnomadNFE')
    gnomad_nfeest = sgqlc.types.Field(Float, graphql_name='gnomadNFEEST')
    gnomad_nfenwe = sgqlc.types.Field(Float, graphql_name='gnomadNFENWE')
    gnomad_nfeseu = sgqlc.types.Field(Float, graphql_name='gnomadNFESEU')
    gnomad_nfeonf = sgqlc.types.Field(Float, graphql_name='gnomadNFEONF')
    gnomad_oth = sgqlc.types.Field(Float, graphql_name='gnomadOTH')


class Version(sgqlc.types.Type):
    __schema__ = graphql_types
    __field_names__ = ('major', 'minor', 'patch')
    major = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='major')
    minor = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='minor')
    patch = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='patch')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
graphql_types.query_type = Query
graphql_types.mutation_type = None
graphql_types.subscription_type = None

