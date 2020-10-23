from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from graphql_types import *

from pandas import json_normalize
import pandas as pd


class Genetics:
    url = 'http://genetics-api.opentargets.io/graphql'
    endpoint = HTTPEndpoint(url)

    def genes_for_variant(self, variants, data_frame=True):
        op = Operation(Query)

        for variant in variants:
            op.genes_for_variant(variant_id=variant, __alias__='alias_' + variant).__fields__()
        data = self.endpoint(op)

        if data_frame:
            return json_normalize([alias for aliases in data['data'].values() for alias in aliases], sep='_')
        else:
            result = (op+data)
            return {x: getattr(result, f'alias_{x}') for x in variants}

    def study_info(self, study_ids, data_frame=True):
        op = Operation(Query)

        for study_id in study_ids:
            s = op.study_info(study_id=study_id, __alias__='alias_' + study_id)
            s.__fields__()

        data = self.endpoint(op)
        if data_frame:
            return pd.json_normalize(data['data'].values(), sep='_')
        else:
            result = (op+data)
            return {x: getattr(result, f'alias_{x}') for x in study_ids}

    def top_overlapped_studies(self, study_ids, data_frame=True):
        op = Operation(Query)

        for study_id in study_ids:
            s = op.top_overlapped_studies(study_id=study_id, __alias__='alias_' + study_id)
            s.__fields__()

        data = self.endpoint(op)
        if data_frame:
            return pd.json_normalize(data['data'].values(), sep='_')
        else:
            result = (op+data)
            return {x: getattr(result, f'alias_{x}') for x in study_ids}

    def manhattan(self, study_ids, data_frame=True):
        op = Operation(Query)

        for study_id in study_ids:
            m = op.manhattan(study_id=study_id, __alias__='alias_' + study_id)

            m.associations.best_genes.gene.id()
            m.associations.best_genes.gene.symbol()
            m.associations.best_coloc_genes.gene.id()
            m.associations.best_coloc_genes.gene.symbol()
            m.associations.best_locus2_genes.gene.id()
            m.associations.best_locus2_genes.gene.symbol()
            m.associations.best_locus2_genes.score()

            m.associations().__fields__()
            m.associations().variant().__fields__()

        data = self.endpoint(op)
        if data_frame:
            dfs = []
            for study, aliases in data['data'].items():
                for alias in aliases['associations']:
                    dfs.append(json_normalize(alias, sep='_').assign(study=study.split('alias_')[1]))
            if dfs:
                return pd.concat(dfs, axis=0).reset_index(drop=True)
        else:
            result = (op+data)
            return {x: getattr(result, f'alias_{x}') for x in study_ids}

    def tag_variants_and_studies_for_index_variant(self, index_variants, study_id=None, data_frame=True):
        op = Operation(Query)

        for index_variant in index_variants:
            s = op.tag_variants_and_studies_for_index_variant(variant_id=index_variant, __alias__='alias_' + index_variant)
            s.associations.study.__fields__('study_id')
            s.associations().__fields__()

        data = self.endpoint(op)

        if data_frame:
            dfs = []
            for variant, aliases in data['data'].items():
                for alias in aliases['associations']:
                    dfs.append(json_normalize(alias, sep='_').assign(queryVariant=variant.split('alias_')[1]))
            if dfs:
                df = pd.concat(dfs, axis=0).reset_index(drop=True)
                if study_id is not None:
                    df = df[df.study_studyId == study_id]
                return df
        else:
            result = (op+data)
            return {x: getattr(result, f'alias_{x}') for x in study_ids}
        
        
    def index_variants_and_studies_for_tag_variant(self, index_variants, study_id=None, data_frame=True):
        op = Operation(Query)

        for index_variant in index_variants:
            s = op.index_variants_and_studies_for_tag_variant(variant_id=index_variant, __alias__='alias_' + index_variant)
            s.associations.study.__fields__('study_id')
            s.associations().__fields__()

        data = self.endpoint(op)

        if data_frame:
            dfs = []
            for variant, aliases in data['data'].items():
                for alias in aliases['associations']:
                    dfs.append(json_normalize(alias, sep='_').assign(queryVariant=variant.split('alias_')[1]))
            if dfs:
                df = pd.concat(dfs, axis=0).reset_index(drop=True)
                if study_id is not None:
                    df = df[df.study_studyId == study_id]
                return df
        else:
            result = (op+data)
            return {x: getattr(result, f'alias_{x}') for x in study_ids}
